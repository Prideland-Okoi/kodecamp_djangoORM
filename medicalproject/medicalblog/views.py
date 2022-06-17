from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import InputForm

def home_view(request):
    context={}
    context['form']=InputForm()
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

# Create your views here.
