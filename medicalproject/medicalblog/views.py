from django.shortcuts import render
from django.http import HttpResponse, request

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def contact_view(request):
    return render(request, 'services.html')

# Create your views here.
