from django import forms
from . import models as test_models


class NewUrlForm(forms.ModelForm):
    class Meta:
        model = test_models.Url
        fields = [
            "urladdress",
        ]


class ChangeDescription(forms.ModelForm):
    class Meta:
        model = test_models.Url
        fields = [
            "description",
        ]


class ChangeUrlTitle(forms.ModelForm):
    class Meta:
        model = test_models.Url
        fields = [
            "urltitle",
        ]


class ChangeWebmarkTitleForm(forms.ModelForm):
    class Meta:
        model = test_models.WebMark
        fields = [
            "title",
        ]


class ChangeRepositoryTitleForm(forms.ModelForm):
    class Meta:
        model = test_models.Repository
        fields = [
            "title",
        ]

