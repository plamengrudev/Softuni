from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Category
from memes.models import Meme

from .forms import CommentForm
from .models import Comment

User = get_user_model()


class CommentFormTests(TestCase):
    def test_comment_rejects_short_body(self):
        form = CommentForm(data={"body": "x"})

        self.assertFalse(form.is_valid())
        self.assertFormError(
            form,
            "body",
            "Comments must contain at least 2 characters."
        )

    def test_comment_strips_surrounding_whitespace(self):
        form = CommentForm(data={"body": "  Great meme  "})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["body"], "Great meme")


class CommentCrudTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(
            username="comment-author",
            password="A-strong-password-2026"
        )
        self.other_user = User.objects.create_user(
            username="comment-outsider",
            password="A-strong-password-2026"
        )
        self.category = Category.objects.create(name="Comment testing")
        self.meme = Meme.objects.create(
            title="Commentable meme",
            image="memes/comment-test.png",
            category=self.category,
            owner=self.author
        )
        self.comment = Comment.objects.create(
            meme=self.meme,
            author=self.author,
            body="Original comment"
        )

    def test_anonymous_user_is_redirected_from_comment_creation(self):
        url = reverse(
            "community:comment-create",
            kwargs={"meme_pk": self.meme.pk}
        )

        response = self.client.get(url)

        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={url}"
        )

    def test_authenticated_user_can_create_comment(self):
        self.client.force_login(self.other_user)
        url = reverse(
            "community:comment-create",
            kwargs={"meme_pk": self.meme.pk}
        )

        response = self.client.post(
            url,
            {"body": "A useful and valid comment"}
        )

        self.assertRedirects(response, self.meme.get_absolute_url())
        self.assertTrue(
            Comment.objects.filter(
                meme=self.meme,
                author=self.other_user,
                body="A useful and valid comment"
            ).exists()
        )

    def test_author_can_edit_comment(self):
        self.client.force_login(self.author)

        response = self.client.post(
            reverse(
                "community:comment-edit",
                kwargs={"pk": self.comment.pk}
            ),
            {"body": "Updated comment"}
        )

        self.assertRedirects(response, self.meme.get_absolute_url())
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, "Updated comment")

    def test_non_author_cannot_edit_comment(self):
        self.client.force_login(self.other_user)

        response = self.client.get(
            reverse(
                "community:comment-edit",
                kwargs={"pk": self.comment.pk}
            )
        )

        self.assertEqual(response.status_code, 403)

    def test_author_can_delete_comment(self):
        self.client.force_login(self.author)

        response = self.client.post(
            reverse(
                "community:comment-delete",
                kwargs={"pk": self.comment.pk}
            )
        )

        self.assertRedirects(response, self.meme.get_absolute_url())
        self.assertFalse(
            Comment.objects.filter(pk=self.comment.pk).exists()
        )

    def test_non_author_cannot_delete_comment(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse(
                "community:comment-delete",
                kwargs={"pk": self.comment.pk}
            )
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Comment.objects.filter(pk=self.comment.pk).exists()
        )