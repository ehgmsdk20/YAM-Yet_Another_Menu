from django.core import validators


class MaxValueMultiFieldValidator(validators.MaxLengthValidator):

    def clean(self, x):
        return len(','.join(x))