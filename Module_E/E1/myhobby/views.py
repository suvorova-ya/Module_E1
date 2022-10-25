from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import ContactForm

class PageHome(ListView):
    model = Post
    template_name = 'myhobby/index.html'
    context_object_name = 'posts'



def about(request):
    return render(request, 'myhobby/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myhobby/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'myhobby/contacts.html',context)