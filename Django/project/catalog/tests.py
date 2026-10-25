from django.test import TestCase

from .forms import CategoryForm
from .models import Category


class CatalogTests(TestCase):
    def test_category_creation_and_str(self):
        category = Category.objects.create(name="Prequel Memes")
        self.assertEqual(str(category), "Prequel Memes")

    def test_category_form_rejects_short_or_reposted_names(self):
        Category.objects.create(name="Doge Lore")

        too_short = CategoryForm(data={"name":"F"})
        self.assertFalse(too_short.is_valid())

        repost_category = CategoryForm(data={"name": "doge lore"})
        self.assertFalse(repost_category.is_valid())