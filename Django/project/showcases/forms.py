from django import forms

from .models import Showcase


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Showcase
        fields = ["title", "description", "memes"]