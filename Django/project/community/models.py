from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Comment(models.Model):
    meme = models.ForeignKey(
        "memes.Meme",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at", "pk"]

    def get_absolute_url(self):
        return reverse("meme-detail", kwargs={"pk": self.meme_id})

    def __str__(self):
        return f"{self.author}: {self.body[:40]}"


class Vote(models.Model):
    class Value(models.IntegerChoices):
        UP = 1, "Up"
        DOWN = -1, "Down"

    meme = models.ForeignKey(
        "memes.Meme",
        on_delete=models.CASCADE,
        related_name="votes"
    )
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="meme_votes"
    )
    value = models.SmallIntegerField(
        choices=Value.choices,
        validators=[MinValueValidator(-1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["meme", "voter"],
                name="unique_meme_vote_per_user"
            )
        ]

    def __str__(self):
        return f"{self.voter} voted {self.get_value_display()} on {self.meme}"


class Report(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Open"
        REVIEWED = "reviewed", "Reviewed"
        DISMISSED = "dismissed", "Dismissed"

    meme = models.ForeignKey(
        "memes.Meme",
        on_delete=models.CASCADE,
        related_name="reports"
    )
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="submitted_reports"
    )
    reason = models.TextField(max_length=1000)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviewed_reports"
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["meme", "reporter"],
                name="unique_open_report_per_user_and_meme"
            )
        ]

    def __str__(self):
        return f"Report by {self.reporter} for {self.meme}"