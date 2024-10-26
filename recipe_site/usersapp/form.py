from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserForm(UserCreationForm):

    # тут мы переопределяем поле пароль, можем поменять название, текс подсказки
    # password1 = forms.CharField(
    #     label='Пароль',
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     help_text='Одна большая буква и т.д.',
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
        }
