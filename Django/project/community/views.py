from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from memes.mixins import OwnerRequiredMixin
from memes.models import Meme

from .forms import CommentForm
from .models import Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "community/comment_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.meme = get_object_or_404(Meme, pk=kwargs["meme_pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meme"] = self.meme
        return context

    def form_valid(self, form):
        form.instance.meme = self.meme
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(
    OwnerRequiredMixin,
    UpdateView
):
    model = Comment
    form_class=CommentForm
    owner_field = "author"
    template_name= "community/comment_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meme"] = self.object.meme
        return context


class CommentDeleteView(
    OwnerRequiredMixin,
    DeleteView
):
    model = Comment
    owner_field = "author"
    template_name = "community/comment_confirm_delete.html"
    success_url= reverse_lazy("home")

    def get_success_url(self):
        return self.object.meme.get_absolute_url()