from django.forms import ModelForm
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        prepopulated_fields = {'slug': ('title',)}

    body = forms.CharField(widget=SummernoteWidget)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'