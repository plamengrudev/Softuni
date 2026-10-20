from django import forms

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