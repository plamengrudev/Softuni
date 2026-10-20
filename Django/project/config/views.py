import random

from django.shortcuts import render


NOT_FOUND_MESSAGES = (
    "This page has vanished somewhere beyond the Outer Rim.",
    "Our astromech searched the star charts, but this destination isn't there.",
    "The coordinates lead to empty space. The page may have taken another jump.",
    "No signal from this page. Even the best bounty hunter couldn't track it down.",
    "This part of the galaxy is still being mapped. Try a different route.",
)


def custom_404(request, exception):
    return render(request,"404.html",
        {"not_found_message": random.choice(NOT_FOUND_MESSAGES)},
        status=404
    )