from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.category_list, name="category-list"),
    path("categories/create/", views.category_create, name="category-create"),
    path('tags/', views.tag_list, name="tag-list"),
    path('tags/create/', views.tag_create, name="tag-create"),
]