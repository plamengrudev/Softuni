from django import forms

from .models import Showcase


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Showcase
        fields = ["title", "description", "memes"]

    title = forms.CharField(
        max_length=80,
        label="Collection title",
        widget=forms.TextInput(attrs={"placeholder": "e.g. Best of October"}),
        error_messages={"required": "A collection needs a title."}
    )

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title

    def clean_memes(self):
        memes = self.cleaned_data["memes"]
        if len(memes) > 20:
            raise forms.ValidationError("A collection can hold at most 20 memes.")
        return memes