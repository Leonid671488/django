from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-group-input",
        "placeholder": "Ваше имя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-group-input",
        "placeholder": "Мин. 8 символов"
    }))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-group-input",
        "placeholder": "Ваше имя"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-group-input",
        "placeholder": "example@mail.com"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-group-input",
        "placeholder": "Мин. 8 символов"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-group-input",
        "placeholder": "Подтверждение пароля"
    }))


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
