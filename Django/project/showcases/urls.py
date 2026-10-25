from django.urls import path

from . import views


urlpatterns = [
    path("collections/", views.CollectionListView.as_view(), name="collection-list"),
    path('collections/create/', views.CollectionCreateView.as_view(), name="collection-create"),
    path("collections/<int:pk>/", views.CollectionDetailView.as_view(), name="collection-detail"),
    path("collections/<int:pk>/edit/", views.CollectionUpdateView.as_view(), name="collection-edit"),
    path("collections/<int:pk>/delete/",views.CollectionDeleteView.as_view(), name="collection-delete")
]