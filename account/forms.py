from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'placeholder': "Введите свой логин",
            'id': "username",
            'class': 'input-xlarge',
        }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'placeholder': "Введите ваш пароль",
            'id': "password",
            'class': "input-xlarge",

        }))
