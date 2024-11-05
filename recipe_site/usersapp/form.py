from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class CustomUserForm(UserCreationForm):

    # тут мы переопределяем поле, можем поменять название, текс подсказки
    email = forms.EmailField(
        required=True,  # Указываем, что поле обязательно
        widget=forms.EmailInput(attrs={'class': 'registration__input'}),
        label='Email',
        help_text='Введите действующий адрес электронной почты.'
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]

        #  тут мы назначаем класс для полей формы
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'registration__input'}),
            'last_name': forms.TextInput(attrs={'class': 'registration__input'}),
            'username': forms.TextInput(attrs={'class': 'registration__input'}),
            'password1': forms.PasswordInput(attrs={'class': 'registration__input'}),
        }
