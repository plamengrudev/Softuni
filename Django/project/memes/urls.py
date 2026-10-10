from django.urls import path

from . import views


urlpatterns = [
    path("memes/",views.meme_list, name="meme-list"),
    path('memes/slideshow/', views.meme_slideshow, name="meme-slideshow"),
    path("memes/create/", views.meme_create, name="meme-create"),
    path('memes/<int:pk>/', views.meme_detail, name="meme-detail"),
]