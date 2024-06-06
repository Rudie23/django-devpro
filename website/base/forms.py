from django import forms
from django.contrib.auth.forms import UserCreationForm
from website.base.models import DevUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = DevUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
