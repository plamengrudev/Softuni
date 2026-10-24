from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse


class NamedModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True
        ordering= ["name"]
        constraints =[ models.UniqueConstraint(Lower("name"), name="unique_lower_%(class)s_name")]


    def meme_count(self):
        return self.memes.count()
    
    def __str__(self):
        return self.name
    


class Category(NamedModel):
    def get_absolute_url(self):
        return reverse("category-detail",kwargs={"pk": self.pk})


class Tag(NamedModel):
    def get_absolute_url(self):
        return reverse("tag-detail",kwargs={"pk": self.pk})
