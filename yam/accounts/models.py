from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField

# Create your models here.
User = get_user_model()

class MSFList(list):

    def __init__(self, choices, *args, **kwargs):
        if(choices):
            self.choices = dict(list(choices))
        else:
            self.choices = None
        super(MSFList, self).__init__(*args, **kwargs)

    def __str__(self):
        if(self.choices == None):
            return ''
        msg_list = [self.choices.get(int(i)) if i.isdigit() else self.choices.get(i) for i in self]
        return ', '.join([str(s) for s in msg_list])


class ChoiceArrayField(ArrayField):

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
            'widget': forms.CheckboxSelectMultiple,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        else:
            return MSFList(self.base_field.choices, map(lambda x: x.strip(), value.lstrip('{').rstrip('}').replace('，', ',').split(',')))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home = models.CharField(max_length=30, blank=True)
    office = models.CharField(max_length=30, blank=True)
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
    allergy = ChoiceArrayField(
            models.CharField(max_length=5, choices=ALLERGY_CHOICES, default='',),
            blank=True, null=True
        )
