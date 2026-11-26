from django.test import TestCase
from catalog.models import Category
from django.contrib.auth import get_user_model

from .models import Meme

User = get_user_model()


class MemeVotingTests(TestCase):
	def setUp(self):
		category = Category.objects.create(name="Voting test")
		self.owner = User.objects.create_user(
			username="voting-owner",
			password="A-strong-password-2026"
			)
		self.meme = Meme.objects.create(
			title="Voting test meme",
			image="memes/voting-test.png",
			category=category,
			owner= self.owner
   			)
		
		

	def test_each_page_token_accepts_only_one_vote(self):
		first_page = self.client.get(f"/memes/{self.meme.pk}/")
		first_token = first_page.context["vote_token"]

		self.client.post(
			f"/memes/{self.meme.pk}/",
			{"vote": "up", "vote_token": first_token},
		)
		self.meme.refresh_from_db()
		self.assertEqual(self.meme.rating, 1)

		self.client.post(
			f"/memes/{self.meme.pk}/",
			{"vote": "down", "vote_token": first_token},
		)
		self.meme.refresh_from_db()
		self.assertEqual(self.meme.rating, 1)

		second_page = self.client.get(f"/memes/{self.meme.pk}/")
		second_token = second_page.context["vote_token"]
		self.client.post(
			f"/memes/{self.meme.pk}/",
			{"vote": "down", "vote_token": second_token},
		)
		self.meme.refresh_from_db()
		self.assertEqual(self.meme.rating, 0)

class MemeSlideshowTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Slideshow test")
        self.owner = User.objects.create_user(
			username="slideshow-owner",
			password="A-strong-password-2026"
		)
        

    def test_top_rating_includes_zero_and_negative_ratings(self):
        positive = Meme.objects.create(
            title="Positive meme",
            image="memes/positive.png",
            category=self.category,
            rating=2,
            owner=self.owner
        )
        zero = Meme.objects.create(
            title="Zero meme",
            image="memes/zero.png",
            category=self.category,
            rating=0,
            owner=self.owner
        )
        negative = Meme.objects.create(
            title="Negative meme",
            image="memes/negative.png",
            category=self.category,
            rating=-1,
            owner= self.owner
        )

        response = self.client.get("/memes/slideshow/?sort=top")

        self.assertEqual(
            list(response.context["memes"]),
            [positive, zero, negative],
        )
        
class MemeOwnershipTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="meme-owner",
            password="A-strong-password-2026"
        )
        self.other_user = User.objects.create_user(
            username="other-member",
            password="A-strong-password-2026"
        )
        self.category = Category.objects.create(name="Ownership test")
        self.meme = Meme.objects.create(
            title="Owner-protected meme",
            image="memes/owner-test.png",
            category=self.category,
            owner=self.owner
        )

    def test_anonymous_user_is_redirected_from_edit(self):
        response = self.client.get(f"/memes/{self.meme.pk}/edit/")

        self.assertRedirects(
            response,
            f"/accounts/login/?next=/memes/{self.meme.pk}/edit/"
        )

    def test_non_owner_cannot_edit_meme(self):
        self.client.force_login(self.other_user)

        response = self.client.get(f"/memes/{self.meme.pk}/edit/")

        self.assertEqual(response.status_code, 403)

    def test_non_owner_cannot_delete_meme(self):
        self.client.force_login(self.other_user)

        response = self.client.post(f"/memes/{self.meme.pk}/delete/")

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Meme.objects.filter(pk=self.meme.pk).exists())

    def test_owner_can_open_edit_page(self):
        self.client.force_login(self.owner)

        response = self.client.get(f"/memes/{self.meme.pk}/edit/")

        self.assertEqual(response.status_code, 200)