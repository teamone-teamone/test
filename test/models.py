from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Content(models.Model):
    # objects = models.Manager()
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None, null=True
    )
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    highlight = models.CharField(max_length=200)
    review = models.TextField(default="")
