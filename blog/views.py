from django.shortcuts import render
from .models import *
# Create your views here.
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