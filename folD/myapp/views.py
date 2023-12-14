from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm

# Create your views here.
def home(request):
    return HttpResponse("hello world!")

@login_required(login_url='login')
def dashboard(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/layouts/layout.html", {})

def login(request):    
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            return LoginView.as_view(template_name="folD/myapp/templates/login.html")(request)
        
    else:
        form = LoginForm()
    
    if request.method == "GET":
        return redirect("http://127.0.0.1:8000/dashboard")
    