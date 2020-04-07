from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from random import randint
a=int()
b=int()
def random():
    global a
    global b
    a=randint(1,10)
    b=randint(1,10)
    cap='Sum of '+str(a)+'+'+str(b)
    return cap

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=['title','content','status','cover']

class CreateUserForm(UserCreationForm):
    sums=random()
    captcha=forms.CharField(required=True,label='Enter Captcha '+sums)
    class Meta:
        model = User
        fields=['username','password1','password2','captcha']

    def clean_captcha(self):
        data =self.cleaned_data.get('captcha')
        if str(a+b) == str(data):
            print('**'*50)
            print('add',a+b)
            print('sum',data)
            print('**'*50)
        else:
            raise forms.ValidationError("Please Enter the Right CAPTCHA")
        return data

