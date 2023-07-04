from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Your username:"}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={"placeholder": "Your password:"}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password:"}))

    class Meta:
        model=User
        fields=['username','password1','password2']
        

