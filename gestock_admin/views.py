from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
import re
from .models import Admin
from django.http import HttpResponse

# Create your views here.

regexMail = r"^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$"

def index(request):
    auth = True
    if request.method == 'POST':
        formulaire = forms.Form(request.POST)
        form = request.POST
        if formulaire.is_valid():
            username = form['login']
            mdp = form['mdp']
            try:
                admin = Admin.objects.get(pseudo=username)
            except:
                admin = False
            user = authenticate(request, username=username, password=mdp)
            if user is not None and user.is_active and admin is not False:
                login(request, user)
                return redirect('admin_login')
            else:
                auth = False
    return render(request, 'index.html', {'auth': auth})

def forgot(request):
    return render(request, 'forgot.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='admin_home')
def deconnexion(request):
    logout(request)
    return redirect('admin_home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='admin_home')
def connected(request):
    admin = Admin.objects.get(pseudo=request.user)
    return render(request, 'connected.html', locals())
