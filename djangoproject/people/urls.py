from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("templates/", views.all),
]
"""
in module people look for urls file
"""
