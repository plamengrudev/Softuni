from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import LoginForm, ProfileForm, RegistrationForm
from .models import User


class RegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")
    success_message = "Your account was created. You can now sign in."


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")
    http_method_names = ["post"]


class ProfileDetailView(DetailView):
    model = User
    template_name = "accounts/profile_detail.html"
    context_object_name = "profile_user"
    slug_field = "username"
    slug_url_kwarg = "username"


class ProfileUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = User
    form_class = ProfileForm
    template_name = "accounts/profile_form.html"
    success_message = "Your profile was updated."

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "accounts:profile-detail",
            kwargs={"username": self.object.username}
        )