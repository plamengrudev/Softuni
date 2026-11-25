from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    display_name = models.CharField(
        max_length=80,
        blank=True,
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.display_name or self.username