from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=['title','content','status','cover']

class CreateUserForm(UserCreationForm):
    captcha=forms.CharField(required=True)
    class Meta:
        model = User
        fields=['username','password1','password2','captcha']
