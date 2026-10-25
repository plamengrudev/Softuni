from django.test import TestCase

from .forms import CollectionForm
from .models import Showcase


class ShowcaseTests(TestCase):
    def test_showcase_creation_and_empty_stash(self):
        stash = Showcase.objects.create(
            title="3 AM coding meltdowns",
            description="When the code works on the first try and you don't trust it.",
        )
        self.assertEqual(str(stash), "3 AM coding meltdowns")
        self.assertEqual(stash.meme_count(), 0)

    def test_collection_form_rejects_tiny_title(self):
        form = CollectionForm(data={"title":"XD", "description": "Needs more effort"})
        self.assertFalse(form.is_valid())