from django.db import models
from django.urls import reverse
from memes.models import Meme
from django.conf import settings

class Showcase(models.Model):
    title = models.CharField(max_length=80)
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collections"
    )

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
        ordering = ["-created_at", "-pk"]
        verbose_name="collection"
        verbose_name_plural= "collections"
    
    def get_absolute_url(self):
        return reverse("collection-detail",kwargs={"pk": self.pk})
    
    def meme_count(self):
        return self.memes.count()


    def __str__(self):
        return self.title

