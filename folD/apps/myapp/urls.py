from django.urls import path, include
from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_expense/", views.add_expense, name="add_expense"),
    path("incomes/", views.incomes, name="incomes"),
    path("settings/", views.settings, name="settings"),
    path('fetch-data/', views.fetch_data_view, name='fetch_data'),
]
