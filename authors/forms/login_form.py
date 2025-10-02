from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
                'placeholder': 'Informe seu usuário'
            })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
                'placeholder': 'digite sua senha'
            })
    )