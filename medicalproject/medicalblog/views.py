from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Post
# Create your views here.

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def service_view(request):
    return render(request, 'services.html')
def Post_details(request):
    return render(requst, 'postdetails.html')
