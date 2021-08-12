from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from . import models as test_models
from . import forms as test_forms
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

# Create your views here.


def home(request):
    return render(request, "repository/repositoryhome.html")


def firsturlpaste(request):
    newRepository = test_models.Repository.objects.create()
    if request.user.is_authenticated:
        newRepository.for_user = request.user
        newRepository.save()

    if request.method == "POST":
        form = test_forms.NewUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            newWebmark = test_models.WebMark.objects.create(
                for_repository=newRepository)
            url.for_webmark = newWebmark
            url.urltitle = url.geturltitle()
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": newRepository.pk}))
    return redirect(
        reverse("test:urlrepository", kwargs={"pk": newRepository.pk}))


def urlrepository(request, pk, html_id=''):
    repository = get_object_or_404(test_models.Repository, pk=pk)
    repolist = []
    search = request.GET.get('title', '')
    if search:
        repolist = test_models.Repository.objects.filter(
            title__icontains=search)
    return render(
        request,
        "repository/urlrepository.html",
        {
            "repository": repository,
            "html_id": html_id,
            "repolist": repolist if repolist else [],
            "search": search
        },
    )


def seerepository(request, pk):
    repository = get_object_or_404(test_models.Repository, pk=pk)
    repolist = []
    search = request.GET.get('title', '')
    if search:
        repolist = test_models.Repository.objects.filter(
            title__icontains=search)
    return render(
        request,
        "repository/seerepository.html",
        {
            "repository": repository,
            "repolist": repolist if repolist else [],
            "search": search
        },
    )


def deleterepository(request, pk):
    repository = get_object_or_404(test_models.Repository, pk=pk)
    repository.delete()
    return redirect(reverse("user:myrepo"))


def newWebmark(request, pk):
    repo = get_object_or_404(test_models.Repository, pk=pk)
    test_models.WebMark.objects.create(for_repository=repo)
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
                reverse("test:urlrepository",
                        kwargs={
                            "pk": pk_repo,
                            "html_id": 'webmark_{}'.format(web.id)
                        }))
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
                reverse("test:urlrepository",
                        kwargs={
                            "pk": pk_repo,
                            "html_id": 'webmark_{}'.format(web.id)
                        }))
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
                reverse("test:urlrepository",
                        kwargs={
                            "pk": pk_repo,
                            "html_id": "urltitle_{}".format(url.pk)
                        }))
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


def changedescription(request, pk_repo, pk_url):
    url = get_object_or_404(test_models.Url, pk=pk_url)
    if request.method == "POST":
        form = test_forms.ChangeDescription(request.POST)
        if form.is_valid():
            description = form.cleaned_data.get("description")
            url.description = description
            url.save()
            return redirect(
                reverse("test:urlrepository",
                        kwargs={
                            "pk": pk_repo,
                            "html_id": "description_{}".format(url.pk)
                        }))
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))
