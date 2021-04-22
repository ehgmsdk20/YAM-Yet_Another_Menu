from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import capfirst

from .fields import MultiSelectFormField
from .validators import MaxValueMultiFieldValidator

ALLERGY_CHOICES = (
        ('SHELL', '갑각류 알레르기'),
        ('NUT', '견과 알레르기'),
        ('EGG', '달걀 알레르기'),
        ('PNUT', '땅콩 알레르기'),
        ('WHEAT', '밀 알레르기'),
        ('FISH', '생선 알레르기'),
        ('MILK', '우유 알레르기'),
        ('CLAM', '조개 알레르기'),
        ('BEAN', '콩 알레르기'),
    )

# Create your models here.
User = get_user_model()

class MSFList(list):

    def __init__(self, choices, *args, **kwargs):
        self.choices = choices
        super(MSFList, self).__init__(*args, **kwargs)

    def __str__(msgl):
        msg_list = [msgl.choices.get(int(i)) if i.isdigit() else msgl.choices.get(i) for i in msgl]
        return u', '.join([str(s) for s in msg_list])

class MultiSelectField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(MultiSelectField, self).__init__(*args, **kwargs)
        if self.max_length is None:
            if self.choices:
                self.max_length = len(','.join([str(key) for key, label in choices]))
        else:
            self.max_length = 200
        self.validators[0] = MaxValueMultiFieldValidator(self.max_length)

    def _get_flatchoices(self):
        flat_choices = super(MultiSelectField, self)._get_flatchoices()

        class MSFFlatchoices(list):
            # Used to trick django.contrib.admin.utils.display_for_field into
            # not treating the list of values as a dictionary key (which errors
            # out)
            def __bool__(self):
                return False
            __nonzero__ = __bool__
        return MSFFlatchoices(flat_choices)
    flatchoices = property(_get_flatchoices)

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def get_choices_selected(self, arr_choices):
        named_groups = arr_choices and isinstance(arr_choices[0][1], (list, tuple))
        choices_selected = []
        if named_groups:
            for choice_group_selected in arr_choices:
                for choice_selected in choice_group_selected[1]:
                    choices_selected.append(str(choice_selected[0]))
        else:
            for choice_selected in arr_choices:
                choices_selected.append(str(choice_selected[0]))
        return choices_selected

    def value_to_string(self, obj):
        try:
            value = self._get_val_from_obj(obj)
        except AttributeError:
            value = super(MultiSelectField, self).value_from_object(obj)
        return self.get_prep_value(value)

    def validate(self, value, model_instance):
        arr_choices = self.get_choices_selected(self.get_choices_default())
        for opt_select in value:
            if (opt_select not in arr_choices):
                raise exceptions.ValidationError(self.error_messages['invalid_choice'] % value)

    def get_default(self):
        default = super(MultiSelectField, self).get_default()
        if isinstance(default, int):
            default = str(default)
        return default

    def formfield(self, **kwargs):
        defaults = {'required': not self.blank,
                    'label': capfirst(self.verbose_name),
                    'help_text': self.help_text,
                    'choices': self.choices,
                    'max_length': self.max_length,}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_prep_value(self, value):
        return '' if value is None else ",".join(map(str, value))

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared and not isinstance(value, str):
            value = self.get_prep_value(value)
        return value

    def to_python(self, value):
        choices = dict(self.flatchoices)

        if value:
            if isinstance(value, list):
                return value
            elif isinstance(value, str):
                value_list = map(lambda x: x.strip(), value.replace(u'，', ',').split(','))
                return MSFList(choices, value_list)
            elif isinstance(value, (set, dict)):
                return MSFList(choices, list(value))
        return MSFList(choices, [])


    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.to_python(value)

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            def get_list(obj):
                fieldname = name
                choicedict = dict(self.choices)
                display = []
                if getattr(obj, fieldname):
                    for value in getattr(obj, fieldname):
                        item_display = choicedict.get(value, None)
                        if item_display is None:
                            try:
                                item_display = choicedict.get(int(value), value)
                            except (ValueError, TypeError):
                                item_display = value
                        display.append(str(item_display))
                return display

            def get_display(obj):
                return ", ".join(get_list(obj))
            get_display.short_description = self.verbose_name

            setattr(cls, 'get_%s_list' % self.name, get_list)
            setattr(cls, 'get_%s_display' % self.name, get_display)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home = models.CharField(max_length=30, blank=True)
    office = models.CharField(max_length=30, blank=True)
    allergy = MultiSelectField(choices=ALLERGY_CHOICES, max_length=5)

