from django.test import TestCase
from catalog.models import Category

from .models import Meme


class MemeVotingTests(TestCase):
	def setUp(self):
		category = Category.objects.create(name="Voting test")
		self.meme = Meme.objects.create(
			title="Voting test meme",
			image="memes/voting-test.png",
			category=category,
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

    def test_top_rating_includes_zero_and_negative_ratings(self):
        positive = Meme.objects.create(
            title="Positive meme",
            image="memes/positive.png",
            category=self.category,
            rating=2,
        )
        zero = Meme.objects.create(
            title="Zero meme",
            image="memes/zero.png",
            category=self.category,
            rating=0,
        )
        negative = Meme.objects.create(
            title="Negative meme",
            image="memes/negative.png",
            category=self.category,
            rating=-1,
        )

        response = self.client.get("/memes/slideshow/?sort=top")

        self.assertEqual(
            list(response.context["memes"]),
            [positive, zero, negative],
        )