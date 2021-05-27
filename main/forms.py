from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class Register_Form(forms.Form):
    email = forms.EmailField(required = True, widget = EmailInput(
        attrs={
            'name':'email',
            'id':'email',
            'class':'form-control',
            'placeholder':'name@example.com',
        }
    ))

    username = forms.CharField(required = True, max_length=30, widget=TextInput(
        attrs={
            'name':'username',
            'id':'username',
            'class':'form-control',
            'placeholder':'username',
        }
    ))

    password1 = forms.CharField(required = True, widget = PasswordInput(
        attrs={
            'name':'password1',
            'id':'password1',
            'class':'form-control',
        }
    ))

    password2 = forms.CharField(required = True, widget = PasswordInput(
        attrs={
            'name':'password2',
            'id':'password2',
            'class':'form-control',
        }
    ))


class Login_Form(forms.Form):
    username = forms.CharField(required = True, max_length=30, widget=TextInput(
        attrs={
            'name':'username',
            'id':'username',
            'class':'form-control',
            'placeholder':'username',
        }
    ))

    password = forms.CharField(widget=PasswordInput(
        attrs={
            'name':'password',
            'id':'password',
            'class':'form-control',
        }
    ))