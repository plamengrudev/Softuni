from django.core.paginator import Paginator


class PaginatedMemesMixin:
    paginate_by = 6
    meme_ordering = None

    def get_memes(self):
        memes = self.object.memes.all()

        if self.meme_ordering:
            memes = memes.order_by(*self.meme_ordering)

        return memes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_memes(), self.paginate_by)
        context["page_obj"] = paginator.get_page(
            self.request.GET.get("page")
        )
        return context