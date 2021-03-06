from django import forms
from django.contrib.auth import get_user_model
from . import models

class UserForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=get_user_model()
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                {'password': ["password and confirm_password does not match",]}
            )

class ProfileForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model=models.Profile
        exclude = ('user',)
        widgets = {
            'home': forms.TextInput(attrs={'placeholder': '주소를 입력하세요.'}),
            'office': forms.TextInput(attrs={'placeholder': '주소를 입력하세요.'}),
        }



