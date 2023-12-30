from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import RegistrationForm

def register_user(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "registration/register.html", context)


def login_user(request):
    context = {}
    return render(request, "folD/accessing/templates/registration/register.html", context)
    
def logout_user(request):
    logout(request)
    return redirect('login')
    
