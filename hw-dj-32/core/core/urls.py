from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('captcha/', include('captcha.urls')),
]
