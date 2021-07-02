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
        "changedescription1/<int:pk_repo>/<int:pk_url>/",
        views.changedescription1,
        name="changedescription1",
    ),
    path(
        "changedescription2/<int:pk_repo>/<int:pk_url>/",
        views.changedescription2,
        name="changedescription2",
    ),
    path(
        "changedescription3/<int:pk_repo>/<int:pk_url>/",
        views.changedescription3,
        name="changedescription3",
    ),
]
