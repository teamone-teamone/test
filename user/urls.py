from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.loginSignUP, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.userlogout, name="logout"),
    path("myrepo/", views.myrepo, name="myrepo"),
]
