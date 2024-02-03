from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.myapp.urls")),
    path("", include("apps.accessing.urls")),
    path("", include("django.contrib.auth.urls")),
]
