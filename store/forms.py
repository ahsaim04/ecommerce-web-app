from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext ,gettext_lazy as _
from django.contrib.auth import password_validation

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Username"),widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))