from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from . import forms
from test import models as test_models


def userlogout(request):
    logout(request)
    return redirect(reverse("test:home"))


def loginSignUP(request):

    if request.user.is_authenticated:
        return redirect(reverse("user:myrepo"))

    login_form = forms.LoginForm(request.POST or None)
    signup_form = forms.SignUpForm(request.POST or None)
    login_info = {"email": ""}
    signup_info = {"email": ""}
    login_error = ""
    signup_error = ""
    isLogin = True
    if request.method == "POST":
        if request.POST.get("nickname"):
            isLogin = False
            if signup_form.is_valid():
                signup_form.save()
                email = signup_form.cleaned_data.get("email")
                password = signup_form.cleaned_data.get("password")
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse("user:myrepo"))
            else:
                nickname = request.POST.get("nickname")
                email = request.POST.get("email")
                signup_info["nickname"] = nickname
                signup_info["email"] = email
                signup_error = list(signup_form.errors.popitem())[1][0]
        else:
            isLogin = True
            if login_form.is_valid():
                email = login_form.cleaned_data.get("email")
                password = login_form.cleaned_data.get("password")
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse("user:myrepo"))
            else:
                email = request.POST.get("email")
                login_info["email"] = email
                login_error = list(login_form.errors.popitem())[1][0]

    return render(
        request,
        "user/login.html",
        {
            "login_form": login_form,
            "login_info": login_info,
            "login_error": login_error,
            "signup_form": signup_form,
            "signup_info": signup_info,
            "signup_error": signup_error,
            "isLogin": isLogin,
        },
    )


def signup(request):

    if request.user.is_authenticated:
        return redirect(reverse("user:myrepo"))

    form = forms.SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
        return redirect(reverse("user:myrepo"))

    return render(
        request,
        "user/signup.html",
        {
            "form": form,
        },
    )


def myrepo(request):
    if not request.user.is_authenticated:
        return redirect(reverse("test:home"))

    mysearch = request.GET.get('search-myrepo', '')
    search = request.GET.get('title', '')
    searchlist = []

    if (search):
        searchlist = test_models.Repository.objects.filter(
            title__icontains=search)
    myrepolist = test_models.Repository.objects.filter(
        for_user=request.user).filter(title__icontains=mysearch)
    return render(
        request, "user/myrepo.html", {
            "myrepolist": myrepolist,
            "mysearch": mysearch,
            "searchlist": searchlist,
            "search": search,
        })
