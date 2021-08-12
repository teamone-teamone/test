from django.urls import path
from . import views

app_name = "test"

urlpatterns = [
    # path("new/", views.new, name="new"),
    path("", views.home, name="home"),
    path("firsturlpaste/", views.firsturlpaste, name="firsturlpaste"),
    path("newWebmark/<int:pk>/", views.newWebmark, name="newWebmark"),
    path("seerepository/<int:pk>", views.seerepository, name="seerepository"),
    path("urlrepository/<int:pk>", views.urlrepository, name="urlrepository"),
    path("urlrepository/<int:pk>/<str:html_id>",
         views.urlrepository,
         name="urlrepository"),
    path("addUrl/<int:pk_repo>/<int:pk_web>/", views.addUrl, name="addUrl"),
    path(
        "changeWebmarkTitle/<int:pk_repo>/<int:pk_web>/",
        views.changeWebmarkTitle,
        name="changeWebmarkTitle",
    ),
    path(
        "deleteWebmark/<int:pk_repo>/<int:pk_web>/",
        views.deleteWebmark,
        name="deleteWebmark",
    ),
    path(
        "deleteUrl/<int:pk_repo>/<int:pk_url>/",
        views.deleteUrl,
        name="deleteUrl",
    ),
    path(
        "changeRepositoryTitle/<int:pk>/",
        views.changeRepositoryTitle,
        name="changeRepositoryTitle",
    ),
    path(
        "deleterepository/<int:pk>/",
        views.deleterepository,
        name="deleterepository",
    ),
    path(
        "changeurltitle/<int:pk_repo>/<int:pk_url>/",
        views.changeurltitle,
        name="changeurltitle",
    ),
    path(
        "changedescription/<int:pk_repo>/<int:pk_url>/",
        views.changedescription,
        name="changedescription",
    ),
]
