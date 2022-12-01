from django import forms
from django.core import validators

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.CharField(max_length=254, validators=[validators.EmailValidator(message="Invalid Email")])
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)