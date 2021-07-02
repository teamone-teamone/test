from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Repository)
admin.site.register(models.WebMark)
admin.site.register(models.Url)
