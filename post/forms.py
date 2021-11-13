from typing import OrderedDict
from django import forms
from django.http import request
from .models import PostModel
class PostForm(forms.ModelForm):
    # author=forms.CharField(max_length=50)
    class Meta:
        model=PostModel
        fields='__all__'

class CreatePostForm(forms.ModelForm):
    # author=forms.CharField(max_length=50)
    class Meta:
        model=PostModel
        fields=['post',]
        # order_by="-id"


    

