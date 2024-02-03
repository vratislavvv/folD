from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add_expense/", views.add_expense, name="add_expense"),
    path("incomes/", views.incomes, name="incomes"),
    path("settings/", views.settings, name="settings"),
]
