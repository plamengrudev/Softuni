from django.shortcuts import render, redirect
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