"""
Form components for account app
"""
from django import forms


class UserRegistrationForm(forms.Form):
    """
    Signup & SignIn form input fields
    """
    username = forms.CharField(label='Username', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(label='Confirm Password',
                                       max_length=50, min_length=5,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))
