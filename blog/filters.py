import django_filters
from .models import *
from django import forms
from django_filters import CharFilter

class PostFilter(django_filters.FilterSet):
    Title= CharFilter(field_name='title', lookup_expr='icontains')
    Author= CharFilter(field_name='author', lookup_expr='icontains')
    class Meta:
        model=Post
        fields=['Title','Author']
        