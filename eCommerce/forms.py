from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label='Confirm Password',
                                      widget=forms.PasswordInput
                                      )

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')
        if password != passwordConfirm:
            raise forms.ValidationError('Passwords must match!')
        return data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        temp = User.objects.filter(username=username)
        if temp.exists():
            raise forms.ValidationError('Username is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        temp = User.objects.filter(email=email)
        if temp.exists():
            raise forms.ValidationError('Email is taken')
        return email