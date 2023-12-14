from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
