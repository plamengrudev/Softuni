from django.urls import path

from . import views

app_name = "community"

urlpatterns = [
    path(
        "memes/<int:meme_pk>/comments/create/",
        views.CommentCreateView.as_view(),
        name="comment-create"
    ),
    path(
        "comments/<int:pk>/edit/",
        views.CommentUpdateView.as_view(),
        name="comment-edit"
    ),
    path(
        "comments/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment-delete"
    )
]