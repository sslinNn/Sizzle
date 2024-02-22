from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-input', 'placeholder': 'Username'}
        ), min_length=4, max_length=25
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-input', 'placeholder': 'Password'}
        ), min_length=6
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}), label='')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password']

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email
