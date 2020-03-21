from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
#login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
#custom decorator
#group management
from django.contrib.auth.models import Group

from .decorators import *

def index(request):
    data=Post.objects.filter(status=1).order_by('-created_on')
    context={
        'data':data
    }
    return render(request,'index.html',context)

def show(request,pk):
    content=Post.objects.filter(id=pk)
    context={
        'content':content
    }
    return render(request,'show.html',context)



@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Userrname or Password is Incorrect')
            return redirect('login')
    context={}
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def signup(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,"User Created Successfully for "+username)
            '''Add group while register bew=low two lines'''
            group= Group.objects.get(name='user')
            user.groups.add(group)
            '''Till herer'''
            '''Auto create a profile of a user'''
            Post.objects.create(author=user)
            '''Till here'''
            return redirect('login')
    context={
            'form':form
        }
    return render(request,'register.html',context)
