from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Category, Tag
from .forms import CategoryForm, TagForm



class CategoryListView(ListView):
    model=Category
    template_name="catalog/category_list.html"
    context_object_name = "categories"



class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class= CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("category-list")
    success_message ="Category created"


class PaginatedMemeDetailView(DetailView):
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object.memes.all(),self.paginate_by)
        context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
        return context

class CategoryDetailView(PaginatedMemeDetailView):
    model = Category
    template_name = "catalog/category_detail.html"


class CategoryDeleteView(SuccessMessageMixin,DeleteView):
    model = Category
    template_name = "catalog/category_confirm_delete.html"
    success_url = reverse_lazy("category-list")
    success_message = "Category deleted"

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request, "This category still has memes and cannot be deleted"
            )
            return HttpResponseRedirect(self.object.get_absolute_url())

class TagListView(ListView):
    model = Tag
    template_name= "catalog/tag_list.html"
    context_object_name = "tags"


class TagCreateView(SuccessMessageMixin,CreateView):
    model = Tag
    form_class=TagForm
    template_name = "catalog/tag_form.html"
    success_url=reverse_lazy("tag-list")
    success_message="Tag created"

class TagDetailView(PaginatedMemeDetailView):
    model = Tag
    template_name = "catalog/tag_detail.html" 

class TagDeleteView(SuccessMessageMixin,DeleteView):
    model = Tag
    template_name= "catalog/tag_confirm_delete.html"
    success_url=reverse_lazy("tag-list")
    success_message = "Tag deleted."