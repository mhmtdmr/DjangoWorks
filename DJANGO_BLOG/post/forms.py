from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['FullName'] 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title','Body','IsPublished','CreateDate','PublishDate','Author','BlogImage']