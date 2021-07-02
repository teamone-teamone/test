from django import forms
from . import models as test_models


class NewUrlForm(forms.ModelForm):
    class Meta:
        model = test_models.Url
        fields = [
            "urladdress",
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


# class ContentEditForm(forms.ModelForm):
#     class Meta:
#         model = Content
#         fields = [
#             "star",
#             "highlight",
#             "review",
#         ]

