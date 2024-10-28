from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomUserForm(UserCreationForm):

    # тут мы переопределяем поле, можем поменять название, текс подсказки
    # email = forms.EmailInput(
        # label='Пароль',
        # strip=False,
        # widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # help_text='Одна большая буква и т.д.',
    # )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            # 'sex',
            'email',
            'username',
        ]

        #  тут мы назначаем класс для полей формы
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'registration__input'}),
            'last_name': forms.TextInput(attrs={'class': 'registration__input'}),
            'email': forms.EmailInput(attrs={'class': 'registration__input', 'blank': 'False'}),
            'username': forms.TextInput(attrs={'class': 'registration__input'}),
            'password1': forms.PasswordInput(attrs={'class': 'registration__input'}),
        }