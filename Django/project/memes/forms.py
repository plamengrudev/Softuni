from django import forms

from .models import Meme, Showcase


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ["title", "image", "category", "tags"]


class ShowcaseForm(forms.ModelForm):
    class Meta:
        model = Showcase
        fields = ["title", "description", "memes"]