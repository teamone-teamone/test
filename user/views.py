from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from . import forms
from test import models as test_models


def userlogout(request):
    logout(request)
    return redirect(reverse("test:home"))


class LoginView(FormView):

    template_name = "user/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("user:myrepo")

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if self.request.user.is_authenticated:
            return redirect(reverse("test:home"))

        return self.render_to_response(self.get_context_data())


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

    return render(request, "user/signup.html", {"form": form,},)


def myrepo(request):
    
    search = request.GET.get('search-myrepo', '')
    repolist = test_models.Repository.objects.filter(for_user=request.user).filter(title__icontains=search)
    return render(request, "user/myrepo.html", {"repolist": repolist,})
