"""mydiary urls linked myproject urls.py"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new/", views.new, name="new"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("deleteensure/<int:pk>", views.deleteensure, name="deleteensure"),

    
]
