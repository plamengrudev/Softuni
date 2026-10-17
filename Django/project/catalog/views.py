from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Tag
from .forms import CategoryForm, TagForm


def category_list(request):
    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "catalog/category_list.html", context)

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("category-list")
    else:
        form = CategoryForm()

    context = {
        "form": form,
    }

    return render(request, "catalog/category_form.html", context)

def category_detail(request,pk):
    category = get_object_or_404(Category,pk=pk)
    paginator= Paginator(category.memes.all(),6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "category": category,
        "page_obj": page_obj
    }

    return render(request,"catalog/category_detail.html",context)


def tag_list(request):
    tags = Tag.objects.all()

    context = {
        "tags": tags,
    }

    return render(request, "catalog/tag_list.html", context)

def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tag-list")
    else:
        form = TagForm()

    context = {
        "form": form,
    }

    return render(request, "catalog/tag_form.html",context)

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    paginator = Paginator(tag.memes.all(),6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "tag": tag,
        "page_obj": page_obj,
    }

    return render(request, "catalog/tag_detail.html", context)