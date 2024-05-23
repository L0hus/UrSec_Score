from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': 'Логин'})
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'placeholder': 'Пароль'})
    )