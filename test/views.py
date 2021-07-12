from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from . import models as test_models
from . import forms as test_forms
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

# Create your views here.


def home(request):

    newRepository = test_models.Repository.objects.create()
    if request.user.is_authenticated:
        newRepository.for_user = request.user
        newRepository.save()
    return redirect(
        reverse("test:urlrepository", kwargs={"pk": newRepository.pk})
    )


def urlrepository(request, pk):
    repository = get_object_or_404(test_models.Repository, pk=pk)

    return render(
        request, "repository/urlrepository.html", {"repository": repository},
    )


def deleterepository(request, pk):
    repository = get_object_or_404(test_models.Repository, pk=pk)
    repository.delete()
    return redirect(reverse("user:myrepo"))


def newUrl(request, pk):
    repo = get_object_or_404(test_models.Repository, pk=pk)
    if request.method == "POST":
        form = test_forms.NewUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            newWebmark = test_models.WebMark.objects.create(for_repository=repo)
            url.for_webmark = newWebmark
            url.urltitle = url.geturltitle()
            url.save()
            return redirect(reverse("test:urlrepository", kwargs={"pk": pk}))
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk}))


def addUrl(request, pk_repo, pk_web):
    web = get_object_or_404(test_models.WebMark, pk=pk_web)
    if request.method == "POST":
        form = test_forms.NewUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.for_webmark = web
            url.urltitle = url.geturltitle()
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def changeWebmarkTitle(request, pk_repo, pk_web):
    web = get_object_or_404(test_models.WebMark, pk=pk_web)
    if request.method == "POST":
        form = test_forms.ChangeWebmarkTitleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            web.title = title
            web.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def deleteWebmark(request, pk_repo, pk_web):
    web = get_object_or_404(test_models.WebMark, pk=pk_web)
    web.delete()
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def deleteUrl(request, pk_repo, pk_url):
    url = get_object_or_404(test_models.Url, pk=pk_url)
    url.delete()
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def changeurltitle(request, pk_repo, pk_url):
    url = get_object_or_404(test_models.Url, pk=pk_url)
    if request.method == "POST":
        form = test_forms.ChangeUrlTitle(request.POST)
        if form.is_valid():
            urltitle = form.cleaned_data.get("urltitle")
            url.urltitle = urltitle
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def changeRepositoryTitle(request, pk):
    repo = get_object_or_404(test_models.Repository, pk=pk)
    if request.method == "POST":
        form = test_forms.ChangeRepositoryTitleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            repo.title = title
            repo.save()
            return redirect(reverse("test:urlrepository", kwargs={"pk": pk}))
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk}))


def changedescription1(request, pk_repo, pk_url):
    url = get_object_or_404(test_models.Url, pk=pk_url)
    if request.method == "POST":
        form = test_forms.ChangeDescription(request.POST)
        if form.is_valid():
            description1 = form.cleaned_data.get("description1")
            description1 = description1.replace("#", "")
            url.description1 = description1
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def changedescription2(request, pk_repo, pk_url):
    url = get_object_or_404(test_models.Url, pk=pk_url)
    if request.method == "POST":
        form = test_forms.ChangeDescription(request.POST)
        if form.is_valid():
            description2 = form.cleaned_data.get("description1")
            description2 = description2.replace("#", "")
            url.description2 = description2
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def changedescription3(request, pk_repo, pk_url):
    url = get_object_or_404(test_models.Url, pk=pk_url)
    if request.method == "POST":
        form = test_forms.ChangeDescription(request.POST)
        if form.is_valid():
            description3 = form.cleaned_data.get("description1")
            description3 = description3.replace("#", "")
            url.description3 = description3
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))
