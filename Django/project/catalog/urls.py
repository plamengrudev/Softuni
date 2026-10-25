from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("categories/<int:pk>/delete/", views.CategoryDeleteView.as_view(), name="category-delete"),
    path('tags/', views.TagListView.as_view(), name="tag-list"),
    path('tags/create/', views.TagCreateView.as_view(), name="tag-create"),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(),name="tag-delete")
]