from django import forms
from .models import Category, Tag


class NamedModelForm(forms.ModelForm):
    min_name_length = 2

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        model = self._meta.model
        verbose = model._meta.verbose_name

        if len(name) < self.min_name_length:
            raise forms.ValidationError(
                f"Name must be at least {self.min_name_length} characters."
            )
        if model.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(f"A {verbose} with this name already exists.")
        return name


class CategoryForm(NamedModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    name = forms.CharField(
        max_length=50,
        label="Category name",
        widget=forms.TextInput(attrs={"placeholder": "e.g. Animals"}),
        error_messages={"required": "Please enter a category name."}
    )


class TagForm(NamedModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

    name = forms.CharField(
        max_length=50,
        label="Tag name",
        widget=forms.TextInput(attrs={"placeholder": "e.g. funny"}),
        error_messages={"required": "Please enter a tag name."}
    )
