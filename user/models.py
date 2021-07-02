from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel

# 중복 로그인 방지
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from importlib import import_module


class User(AbstractUser, TimeStampedModel):
    """custom user """

    nickname = models.CharField(max_length=50, null=False)

