from django.forms import ModelForm 
from django import forms
from .models import *


class PhotoForm(ModelForm):    
    class Meta:
        model = Photo
        fields = ("preview_text","title","thumbnail","tag","description",)

        
