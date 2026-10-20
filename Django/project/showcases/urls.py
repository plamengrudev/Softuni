from django.urls import path

from . import views


urlpatterns = [
    path("collections/", views.collection_list, name="collection-list"),
    path('collections/create/', views.collection_create, name="collection-create"),
    path("collections/<int:pk>/", views.collection_detail, name="collection-detail"),
    path("collections/<int:pk>/edit/", views.collection_edit, name="collection-edit"),
    path("collections/<int:pk>/delete/",views.collection_delete, name="collection-delete")
]