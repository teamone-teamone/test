from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from . import models as test_models
from . import forms as test_forms
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    newRepository = test_models.Repository.objects.create()

    return redirect(
        reverse("test:urlrepository", kwargs={"pk": newRepository.pk})
    )


def urlrepository(request, pk):
    repository = get_object_or_404(test_models.Repository, pk=pk)

    return render(
        request, "repository/urlrepository.html", {"repository": repository},
    )


def newUrl(request, pk):
    repo = get_object_or_404(test_models.Repository, pk=pk)
    if request.method == "POST":
        form = test_forms.NewUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            newWebmark = test_models.WebMark.objects.create(for_repository=repo)
            url.for_webmark = newWebmark
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
            url.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


def addUrl(request, pk_repo, pk_web):
    repo = get_object_or_404(test_models.Repository, pk=pk_repo)
    web = get_object_or_404(test_models.WebMark, pk=pk_web)
    if request.method == "POST":
        form = test_forms.NewUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.for_webmark = web
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


def changeRepositoryTitle(request, pk_repo):
    repo = get_object_or_404(test_models.Repository, pk=pk_repo)
    if request.method == "POST":
        form = test_forms.ChangeRepositoryTitleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            repo.title = title
            repo.save()
            return redirect(
                reverse("test:urlrepository", kwargs={"pk": pk_repo})
            )
    return redirect(reverse("test:urlrepository", kwargs={"pk": pk_repo}))


# def new(request):
#     if request.method == "POST":
#         form = ContentForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect("home")
#     else:
#         form = ContentForm()
#     return render(request, "mydiary/new.html", {"form": form})


# def detail(request, pk):
#     post = get_object_or_404(Content, pk=pk)
#     return render(request, "mydiary/detail.html", {"post": post})


# def edit(request, pk):
#     post = get_object_or_404(Content, pk=pk)
#     if request.method == "POST":
#         form = ContentEditForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect("detail", pk=post.pk)
#     else:
#         form = ContentEditForm(instance=post)
#         return render(request, "mydiary/edit.html", {"post":post, "form": form})


# def delete(request, pk):
#     post = get_object_or_404(Content, pk=pk)
#     post.delete()
#     return redirect("home")

# def deleteensure(request, pk):
#     post = get_object_or_404(Content, pk=pk)
#     return render(request, "mydiary/deleteensure.html", {"post": post})
