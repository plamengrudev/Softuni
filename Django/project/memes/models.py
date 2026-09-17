from django.db import models


class Meme(models.Model):
    title = models.CharField(max_length=80)

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

    def __str__(self):
        return self.title