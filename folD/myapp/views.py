from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello world!")

def template(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/index.html", {})

def dashboard(request):
    return render(request, "/workspaces/gradeproject/folD/myapp/templates/layouts/layout.html", {})