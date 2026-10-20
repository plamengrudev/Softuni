from django.urls import path

from . import views


urlpatterns = [
    path('memes/slideshow/', views.meme_slideshow, name="meme-slideshow"),
    path("memes/create/", views.meme_create, name="meme-create"),
    path('memes/<int:pk>/edit/', views.meme_edit,name="meme-edit"),
    path('memes/<int:pk>/delete/', views.meme_delete,name="meme-delete"),
    path('memes/<int:pk>/', views.meme_detail, name="meme-detail"),
]