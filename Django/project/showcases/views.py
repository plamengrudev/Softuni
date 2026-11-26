from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .forms import CollectionForm
from .models import Showcase
from memes.mixins import PaginatedMemesMixin, AuthenticatedCreateMixin, OwnerRequiredMixin


class CollectionListView(ListView):
    model = Showcase
    template_name = "showcases/collection_list.html"
    context_object_name="collections"


class CollectionCreateView(AuthenticatedCreateMixin, SuccessMessageMixin, CreateView):
    model = Showcase
    form_class=CollectionForm
    template_name="showcases/collection_form.html"
    success_url= reverse_lazy("collection-list")
    success_message = "Collection created"
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CollectionUpdateView(OwnerRequiredMixin, SuccessMessageMixin, UpdateView):
    model= Showcase
    form_class=CollectionForm
    template_name= "showcases/collection_form.html"
    context_object_name = "collection"
    success_message= "Collection updated"

class CollectionDetailView(PaginatedMemesMixin, DetailView):
    model = Showcase
    template_name = "showcases/collection_detail.html"
    context_object_name="collection"
    meme_ordering = ("pk",)


class CollectionDeleteView(OwnerRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Showcase
    template_name = "showcases/collection_confirm_delete.html"
    context_object_name = "collection"
    success_url = reverse_lazy("collection-list")
    success_message = "Collection deleted"