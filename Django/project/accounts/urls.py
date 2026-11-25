from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path(
        "profile/edit/",
        views.ProfileUpdateView.as_view(),
        name="profile-edit"
    ),
    path(
        "profile/<str:username>/",
        views.ProfileDetailView.as_view(),
        name="profile-detail"
    )
]