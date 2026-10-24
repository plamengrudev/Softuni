from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class MemeQuerySet(models.QuerySet):
    def popular(self):
        return self.filter(rating__gt=0).order_by("-rating")

class Meme(models.Model):
    title = models.CharField(max_length=80)

    image = models.ImageField(
        upload_to="memes/",
    )

    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.PROTECT,
        related_name="memes",
    )

    tags = models.ManyToManyField(
        "catalog.Tag",
        blank=True,
        related_name="memes",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    objects = MemeQuerySet.as_manager()

    class Meta:
        ordering = ["-created_at", "-pk"]

    def clean(self):
        errors = {}
        if self.title and len(self.title.strip()) < 3:
            errors["title"] = "Title must be at least 3 characters long."
        if errors:
            raise ValidationError(errors)
        
    def get_absolute_url(self):
        return reverse("meme-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    