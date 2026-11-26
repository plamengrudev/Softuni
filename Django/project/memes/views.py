import logging
import secrets

from django.contrib import messages
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import MemeForm
from .models import Meme

logger = logging.getLogger(__name__)


def remove_stored_file(storage, name):
    try:
        storage.delete(name)
    except OSError:
        logger.exception("Could not delete stored image %r", name)
    
def save_meme_form(form):
    try:
        return form.save()
    except OSError:
        form.add_error("image","The image could not be saved. Please try again")
        return None


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
        else:
            messages.warning(request, "Your vote was not counted.")

        return redirect("meme-detail", pk=meme.pk)

    vote_token = secrets.token_urlsafe(24)

    context = {
        "meme": meme,
        "vote_token": vote_token
    }

    return render(request, "memes/meme_detail.html", context)

@login_required
def meme_create(request):
    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.owner = request.user
            if save_meme_form(form):
                messages.success(request, "Meme created")
                return redirect("meme-slideshow")
    else:
        form = MemeForm()

    context = {
        "form": form
    }

    return render(request, "memes/meme_form.html", context)

def meme_slideshow(request):
    if request.GET.get("sort")=="top":
        memes= Meme.objects.popular()
    else:
        memes = Meme.objects.all()

    return render(request, "memes/meme_slideshow.html", {"memes": memes})

@login_required
def meme_edit(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    if meme.owner != request.user and not request.user.is_staff:
        raise PermissionDenied
    
    old_image = meme.image.name

    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES, instance=meme)

        if form.is_valid():
            saved_meme= save_meme_form(form)
            
            if saved_meme:
                if old_image and old_image !=saved_meme.image.name:
                    remove_stored_file(saved_meme.image.storage, old_image)
                
                messages.success(request, "Meme updated")
                return redirect("meme-detail", pk=saved_meme.pk)
    else:
        form=MemeForm(instance=meme)
    
    return render(request,"memes/meme_edit.html",{"form":form, "meme":meme})

@login_required
def meme_delete(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    if meme.owner != request.user and not request.user.is_staff:
        raise PermissionDenied

    if request.method == "POST":
        storage, image_name = meme.image.storage, meme.image.name
        meme.delete()
        if image_name:
            remove_stored_file(storage, image_name)
        messages.success(request, "Meme deleted.")
        return redirect("meme-slideshow")
    
    return render(
        request,
        "memes/meme_confirm_delete.html",
        {"meme":meme}
    )