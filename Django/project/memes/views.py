from django.shortcuts import redirect, render, get_object_or_404

from .forms import MemeForm
from .models import Meme


def home(request):
    return render(request, "home.html")


def meme_list(request):
    memes = Meme.objects.all()

    context = {
        "memes": memes,
    }

    return render(request, "memes/meme_list.html", context)


def meme_detail(request, pk):
    meme = get_object_or_404(Meme, pk=pk)

    context = {
        "meme": meme,
    }

    return render(request, "memes/meme_detail.html", context)


def meme_create(request):
    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("meme-list")
    else:
        form = MemeForm()

    context = {
        "form": form,
    }

    return render(request, "memes/meme_form.html", context)