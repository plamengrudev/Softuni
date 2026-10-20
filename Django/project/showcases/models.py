from django.db import models

from memes.models import Meme


class Showcase(models.Model):
    title = models.CharField(max_length=80)

    description = models.TextField(blank=True)

    memes = models.ManyToManyField(
        Meme,
        blank=True,
        related_name="showcases",
        db_table="memes_showcase_memes",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "memes_showcase"

    def __str__(self):
        return self.title

