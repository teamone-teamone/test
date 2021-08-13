from __future__ import unicode_literals
from django.forms.widgets import ChoiceWidget
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models
from user import models as user_models
from urllib.request import urlopen
from bs4 import BeautifulSoup

# importing the module for url title by chans
from mechanize import Browser

# Create your models here.


class Repository(core_models.TimeStampedModel):
    isopen_CHOICES = (("yes", "yes"), ("no", "no"))
    # objects = models.Manager()
    title = models.CharField(max_length=50, default="", null=True)
    isopen = models.CharField(max_length=10,
                              choices=isopen_CHOICES,
                              default="yes")
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
    title = models.CharField(max_length=50, default="", null=True)


class Url(core_models.TimeStampedModel):
    for_webmark = models.ForeignKey("WebMark",
                                    related_name="url",
                                    on_delete=models.CASCADE)
    urltitle = models.CharField(max_length=100, default="", null=True)
    urladdress = models.CharField(max_length=300, default="", null=True)
    description = models.CharField(max_length=1000, default="", null=True)

    def geturltitle(self):
        if "chans.pythonanywhere" in self.urladdress:
            return self.urladdress
        try:
            br = Browser()
            br.set_handle_equiv(False)
            br.set_handle_robots(False)
            br.addheaders = [(
                'User-agent',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
            )]
            br.open(self.urladdress)
            title = br.title()
        except Exception as e:
            print(e)
            title = self.urladdress
        return title
