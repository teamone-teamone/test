"""mydiary urls linked myproject urls.py"""
from django.urls import path
from . import views

app_name = "test"

urlpatterns = [
    path("", views.home, name="home"),
    # path("new/", views.new, name="new"),
    path("urlrepository/<int:pk>/", views.urlrepository, name="urlrepository"),
    path("newUrl/<int:pk>/", views.newUrl, name="newUrl"),
    path("addUrl/<int:pk_repo>/<int:pk_web>/", views.addUrl, name="addUrl"),
    path(
        "changeWebmarkTitle/<int:pk_repo>/<int:pk_web>/",
        views.changeWebmarkTitle,
        name="changeWebmarkTitle",
    ),
    path(
        "changeRepositoryTitle/<int:pk_repo>/",
        views.changeRepositoryTitle,
        name="changeRepositoryTitle",
    ),
    # path("edit/<int:pk>", views.edit, name="edit"),
    # path("delete/<int:pk>", views.delete, name="delete"),
    # path("deleteensure/<int:pk>", views.deleteensure, name="deleteensure"),
]
