from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("myapp.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("accessing/", include("accessing.urls"))
]
