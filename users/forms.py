from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields


User=get_user_model()


class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput, max_length=50)
    class Meta:
        model=User
        fields=["username",'password']
class SignupForm(forms.Form):
    username=forms.CharField(max_length=50)
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput,label="Password")
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput,label="Confirm Password")
    

    