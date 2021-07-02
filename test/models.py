from __future__ import unicode_literals
from django.forms.widgets import ChoiceWidget
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models
from user import models as user_models

# Create your models here.


class Repository(core_models.TimeStampedModel):
    isopen_CHOICES = (("yes", "yes"), ("no", "no"))
    # objects = models.Manager()
    title = models.CharField(max_length=50, default="Repository title")
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
    title = models.CharField(max_length=50, default="WebMark name")


class Url(core_models.TimeStampedModel):
    for_webmark = models.ForeignKey(
        "WebMark", related_name="url", on_delete=models.CASCADE
    )
    urladdress = models.CharField(max_length=300, default="")
    description1 = models.CharField(max_length=10, default="")
    description2 = models.CharField(max_length=10, default="")
    description3 = models.CharField(max_length=10, default="")
