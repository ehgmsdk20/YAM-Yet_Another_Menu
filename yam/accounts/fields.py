from django import forms

from .validators import MaxValueMultiFieldValidator


class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.max_length = kwargs.pop('max_length', None)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)
        self.validators.append(MaxValueMultiFieldValidator(self.max_length))