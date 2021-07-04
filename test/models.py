from __future__ import unicode_literals
from django.forms.widgets import ChoiceWidget
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models
from user import models as user_models
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your models here.


class Repository(core_models.TimeStampedModel):
    isopen_CHOICES = (("yes", "yes"), ("no", "no"))
    # objects = models.Manager()
    title = models.CharField(max_length=50, default="New Repo title")
    isopen = models.CharField(
        max_length=10, choices=isopen_CHOICES, default="yes"
    )
    likenum = models.IntegerField(default=0)
    for_user = models.ForeignKey(
        user_models.User,
        related_name="repository",
        on_delete=models.CASCADE,
        null=True,
    )


class WebMark(core_models.TimeStampedModel):
    for_repository = models.ForeignKey(
        "Repository",
        related_name="webmark",
        on_delete=models.CASCADE,
        null=False,
    )
    title = models.CharField(max_length=50, default="New WebMark Title")


class Url(core_models.TimeStampedModel):
    for_webmark = models.ForeignKey(
        "WebMark", related_name="url", on_delete=models.CASCADE
    )
    urltitle = models.CharField(max_length=100, default="")
    urladdress = models.CharField(max_length=300, default="")
    description1 = models.CharField(max_length=10, default="")
    description2 = models.CharField(max_length=10, default="")
    description3 = models.CharField(max_length=10, default="")

    def geturltitle(self):
        try:

            html = urlopen(self.urladdress)
            bsObject = BeautifulSoup(html, "html.parser")
            title = bsObject.find("title").text
        except:
            title = self.urladdress
        return title
