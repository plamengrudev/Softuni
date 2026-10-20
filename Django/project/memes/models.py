from django.db import models


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

    def __str__(self):
        return self.title