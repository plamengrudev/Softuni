from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator

from .forms import MemeForm, ShowcaseForm
from .models import Meme,Showcase


def home(request):
    return render(request, "home.html")


def meme_detail(request, pk):
    meme = get_object_or_404(Meme, pk=pk)

    context = {
        "meme": meme
    }

    return render(request, "memes/meme_detail.html", context)


def meme_create(request):
    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("meme-slideshow")
    else:
        form = MemeForm()

    context = {
        "form": form,
    }

    return render(request, "memes/meme_form.html", context)

def meme_slideshow(request):
    memes = Meme.objects.all()

    return render(
        request,
        "memes/meme_slideshow.html",
        {"memes": memes}
    )

def meme_edit(request, pk):
    meme = get_object_or_404(Meme, pk=pk)

    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES, instance=meme)

        if form.is_valid():
            form.save()
            return redirect("meme-detail", pk=meme.pk)
    else:
        form=MemeForm(instance=meme)
    
    return render(request,"memes/meme_edit.html",{"form":form, "meme":meme})

def meme_delete(request, pk):
    meme = get_object_or_404(Meme, pk=pk)

    if request.method == "POST":
        meme.delete()
        return redirect("meme-slideshow")
    
    return render(
        request,
        "memes/meme_confirm_delete.html",
        {"meme":meme}
    )

def showcase_list(request):
    showcases = Showcase.objects.all()

    return render(
        request,
        "memes/showcase_list.html",
        {"showcases": showcases}
    )


def showcase_create(request):
    if request.method == "POST":
        form = ShowcaseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("showcase-list")
    else:
        form = ShowcaseForm()

    return render(
        request,
        "memes/showcase_form.html",
        {"form": form}
    )

def showcase_detail(request, pk):
    showcase = get_object_or_404(Showcase, pk=pk)
    all_memes= showcase.memes.all()
    paginator = Paginator(all_memes, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "memes/showcase_detail.html",
                  {
                      "showcase": showcase,
                      "page_obj": page_obj
                  })

def showcase_edit(request, pk):
    showcase = get_object_or_404(Showcase, pk=pk)

    if request.method == "POST":
        form = ShowcaseForm(request.POST, instance=showcase)

        if form.is_valid():
            form.save()
            return redirect("showcase-detail", pk=showcase.pk)
    else:
        form = ShowcaseForm(instance=showcase)

    return render(request, "memes/showcase_form.html",
                  {
                      "form": form,
                      "showcase": showcase
                  })

def showcase_delete(request,pk):
    showcase = get_object_or_404(Showcase, pk=pk)

    if request.method == "POST":
        showcase.delete()
        return redirect("showcase-list")
    
    return render(request,"memes/showcase_confirm_delete.html",
                  {
                      "showcase":showcase
                  })