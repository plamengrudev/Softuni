from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator

from .forms import CollectionForm
from .models import Showcase


def collection_list(request):
    collections = Showcase.objects.all()

    return render(
        request,
        "showcases/collection_list.html",
        {"collections": collections}
    )


def collection_create(request):
    if request.method == "POST":
        form = CollectionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("collection-list")
    else:
        form = CollectionForm()

    return render(
        request,
        "showcases/collection_form.html",
        {"form": form}
    )

def collection_detail(request, pk):
    collection = get_object_or_404(Showcase, pk=pk)
    all_memes = collection.memes.order_by("pk")
    paginator = Paginator(all_memes, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "showcases/collection_detail.html",
                  {
                      "collection": collection,
                      "page_obj": page_obj
                  })

def collection_edit(request, pk):
    collection = get_object_or_404(Showcase, pk=pk)

    if request.method == "POST":
        form = CollectionForm(request.POST, instance=collection)

        if form.is_valid():
            form.save()
            return redirect("collection-detail", pk=collection.pk)
    else:
        form = CollectionForm(instance=collection)

    return render(request, "showcases/collection_form.html",
                  {
                      "form": form,
                      "collection": collection
                  })

def collection_delete(request,pk):
    collection = get_object_or_404(Showcase, pk=pk)

    if request.method == "POST":
        collection.delete()
        return redirect("collection-list")
    
    return render(request,"showcases/collection_confirm_delete.html",
                  {
                      "collection":collection
                  })

