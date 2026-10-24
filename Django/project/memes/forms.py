from django import forms

from catalog.models import Tag
from .models import Meme


class MemeForm(forms.ModelForm):
    created_at = forms.DateTimeField(label="Created",disabled=True,required=False)


    class Meta:
        model = Meme
        fields = ["title", "image", "category", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        if self.instance.pk:
            self.initial["created_at"] = self.instance.created_at
        else:
            self.fields.pop("created_at")

    title = forms.CharField(
        max_length=80,
        label="Meme title",
        widget=forms.TextInput(attrs={"placeholder": "e.g. Distracted Boyfriend"}),
        error_messages={
            "required": "A meme needs a title.",
            "max_length": "Title is too long (max 80 characters)."
        }
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text="Hold Ctrl to select several tags (max 5)."
    )

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        duplicates = Meme.objects.filter(title__iexact=title).exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise forms.ValidationError("A meme with this title already exists.")
        return title

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and getattr(image, "size", 0) > 5 * 1024 * 1024:
            raise forms.ValidationError("Image must be smaller than 5 MB.")
        return image

    def clean(self):
        cleaned = super().clean()
        tags = cleaned.get("tags")
        if tags and len(tags) > 5:
            self.add_error("tags", "You can select at most 5 tags.")
        return cleaned