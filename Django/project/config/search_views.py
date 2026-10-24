from django.shortcuts import render
from django.urls import reverse

from catalog.models import Category, Tag
from memes.models import Meme
from showcases.models import Showcase


def find_matches(query, limit=None):
    results = []
    searches = (
        (Meme.objects.filter(title__icontains=query).order_by("title"), "Meme", "match-meme", "meme-detail"),
        (Category.objects.filter(name__icontains=query).order_by("name"), "Category", "match-category", "category-detail"),
        (Showcase.objects.filter(title__icontains=query).order_by("title"), "Collection", "match-collection", "collection-detail"),
        (Tag.objects.filter(name__icontains=query).order_by("name"), "Tag", "match-tag", "tag-detail"),
    )

    for queryset, match_type, match_class, route_name in searches:
        if limit is not None:
            queryset = queryset[:limit]

        for item in queryset:
            results.append({
                "title": item.title if isinstance(item, (Meme, Showcase)) else item.name,
                "match_type": match_type,
                "match_class": match_class,
                "url": reverse(route_name, args=[item.pk]),
            })

    return results


def search_suggestions(request):
    query = request.GET.get("q", "").strip()[:100]
    results = find_matches(query, limit=4) if len(query) >= 2 else []

    return render(
        request,
        "search/_suggestions.html",
        {"query": query, "results": results},
    )


def search_results(request):
    query = request.GET.get("q", "").strip()[:100]
    results = find_matches(query) if query else []

    return render(
        request,
        "search/results.html",
        {"query": query, "results": results},
    )
