from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class OwnerRequiredMixin(UserPassesTestMixin):
    owner_field = "owner"
    permission_denied_message = (
        "You can manage only your own content."
    )

    def test_func(self):
        object_to_check = self.get_object()
        owner = getattr(object_to_check, self.owner_field)

        return (
            self.request.user.is_authenticated
            and (
                owner == self.request.user
                or self.request.user.is_staff
            )
        )


class AuthenticatedCreateMixin(LoginRequiredMixin):
    pass