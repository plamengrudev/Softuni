from django.test import TestCase
from django.contrib.auth import get_user_model

from .forms import CollectionForm
from .models import Showcase

User = get_user_model()

class ShowcaseTests(TestCase):
    def test_showcase_creation_and_empty_stash(self):
        owner = User.objects.create_user(username="collection-owner", password="A-strong-password-2026")        
        stash = Showcase.objects.create(
            title="3 AM coding meltdowns",
            description="When the code works on the first try and you don't trust it.",
            owner=owner
        )
        self.assertEqual(str(stash), "3 AM coding meltdowns")
        self.assertEqual(stash.meme_count(), 0)

    def test_collection_form_rejects_tiny_title(self):
        form = CollectionForm(data={"title":"XD", "description": "Needs more effort"})
        self.assertFalse(form.is_valid())
        
class CollectionOwnershipTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="collection-manager",
            password="A-strong-password-2026"
        )
        self.other_user = User.objects.create_user(
            username="collection-outsider",
            password="A-strong-password-2026"
        )
        self.collection = Showcase.objects.create(
            title="Private management test",
            owner=self.owner
        )

    def test_anonymous_user_is_redirected_from_edit(self):
        response = self.client.get(
            f"/collections/{self.collection.pk}/edit/"
        )

        self.assertRedirects(
            response,
            f"/accounts/login/?next=/collections/"
            f"{self.collection.pk}/edit/"
        )

    def test_non_owner_cannot_edit_collection(self):
        self.client.force_login(self.other_user)

        response = self.client.get(
            f"/collections/{self.collection.pk}/edit/"
        )

        self.assertEqual(response.status_code, 403)

    def test_non_owner_cannot_delete_collection(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            f"/collections/{self.collection.pk}/delete/"
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Showcase.objects.filter(pk=self.collection.pk).exists()
        )