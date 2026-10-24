import secrets

from django.db.models import F
from django.shortcuts import redirect, render, get_object_or_404

from .forms import MemeForm
from .models import Meme


def home(request):
    return render(request, "home.html")


def meme_detail(request, pk):
    meme = get_object_or_404(Meme, pk=pk)

    if request.method == "POST":
        vote = request.POST.get("vote")
        vote_token = request.POST.get("vote_token")
        used_tokens = request.session.get("meme_vote_tokens", [])

        if vote in ("up", "down") and vote_token and vote_token not in used_tokens:
            rating_change = 1 if vote == "up" else -1
            Meme.objects.filter(pk=meme.pk).update(rating=F("rating") + rating_change)
            request.session["meme_vote_tokens"] = (used_tokens + [vote_token])[-500:]

        return redirect("meme-detail", pk=meme.pk)

    vote_token = secrets.token_urlsafe(24)

    context = {
        "meme": meme,
        "vote_token": vote_token
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
        "form": form
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