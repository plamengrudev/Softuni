"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve

from memes.views import meme_slideshow
from config.search_views import search_results, search_suggestions

handler404 = "config.views.custom_404"
handler500 = "config.views.custom_500"

urlpatterns = [
    path("", meme_slideshow, name="home"),
    path("admin/", admin.site.urls),
    path("search/", search_results, name="search-results"),
    path("search/suggestions/", search_suggestions, name="search-suggestions"),
    path("",include("catalog.urls")),
    path("", include("memes.urls")),
    path("", include("showcases.urls"))
]

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT}
    )
]
