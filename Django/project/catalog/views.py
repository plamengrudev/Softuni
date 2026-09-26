from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm


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