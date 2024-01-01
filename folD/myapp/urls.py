from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_expense/", views.add_expense, name="add_expense"),
    path("templates/", views.templates, name="templates"),
    path("settings/", views.settings, name="settings"),
]
