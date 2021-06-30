from django import forms
from .models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = [
            "title",
            "user",
            "image",
            "star",
            "highlight",
            "review",
        ]

class ContentEditForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = [
            "star",
            "highlight",
            "review",
        ]

