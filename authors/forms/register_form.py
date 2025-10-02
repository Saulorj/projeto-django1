
from django import forms
from django.contrib.auth.models import User

from app.helpers.form_helper import strong_password


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField( required=True,
                                validators=[strong_password],
                                widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita sua senha'
    }))
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if 'saulo' in data:
            raise forms.ValidationError(
                'O nome não pode ser saulo',
                code = 'invalid'
            )
        return data

    def clean_email(self):
        email_frm = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email_frm).exists()
        if exists:
            raise forms.ValidationError('Email já está em uso!', code='invalid')
        return email_frm


    def clean(self):
        data = super().clean()
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError(
                {'password':'As senhas devem ser iguais'},
                code = 'invalid'
            )
        return data


    class Meta:
        model= User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password',
                  'email',]
        labels = {
            'first_name': '▶️ Nome',
            'last_name':'▶️ Sobrenome',
            'username': '👤 Usuário',
            'password':'🔒 Senha',
            'email': '📧 E-mail'
        }

        help_texts = {
            'email': ''
        }

        error_messages = {
            'username': {
                'required': '❌ O usuário é obrigatório'
            }
        }

        #sobrescreve itens de usabilidade do campo
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'digite seu nome',
                'class': 'input-name'
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'digite seu sobrenome'
            }),
            # troca o input de text para password
            'password': forms.PasswordInput(attrs={
                'placeholder': 'digite sua senha'
            })
        }
