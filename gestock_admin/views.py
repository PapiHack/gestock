from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def forgot(request):
    return render(request, 'forgot.html')