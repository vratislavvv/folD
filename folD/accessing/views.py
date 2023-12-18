from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['LOGIN_username']
        password = request.POST['LOGIN_password']
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated User: {user}")


        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(request, ("Something went wrong, try again later"))
            return redirect('login')

    if request.method == "GET":
        return render(request, 'authentification/login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('login')
    
