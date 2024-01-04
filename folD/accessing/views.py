from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import RegistrationForm
from myapp.models import Bank

def register_user(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    else:
        form = RegistrationForm()

        if request.method == "POST":
            form = RegistrationForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                bank_append = Bank(username=user.username, balance=0.0)
                bank_append.save()

                return redirect('login')  

        context = {'form': form}
        return render(request, "registration/register.html", context)


def login_user(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Incorrect login data.')

        context = {}
        return render(request, "registration/login.html", context)


def logout_user(request): 
    logout(request)
    return redirect('login')
