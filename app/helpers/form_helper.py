import re

from django import forms


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise forms.ValidationError('Senha deve conter minimo de 8 caracteres com letras e numeros.', code = 'invalid')