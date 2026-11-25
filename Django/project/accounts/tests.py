from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class RegistrationTests(TestCase):
    def test_registration_creates_user(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "new-member",
                "email": "member@example.com",
                "display_name": "New Member",
                "password1": "A-strong-password-2026",
                "password2": "A-strong-password-2026"
            }
        )

        self.assertRedirects(response, reverse("accounts:login"))
        self.assertTrue(
            User.objects.filter(username="new-member").exists()
        )

    def test_registration_rejects_duplicate_email(self):
        User.objects.create_user(
            username="existing-member",
            email="member@example.com",
            password="A-strong-password-2026"
        )

        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "second-member",
                "email": "MEMBER@example.com",
                "display_name": "Second Member",
                "password1": "Another-strong-password-2026",
                "password2": "Another-strong-password-2026"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            User.objects.filter(username="second-member").exists()
        )
        self.assertFormError(
            response.context["form"],
            "email",
            "An account with this email already exists."
        )


class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test-member",
            email="test@example.com",
            password="A-strong-password-2026"
        )

    def test_user_can_login(self):
        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "test-member",
                "password": "A-strong-password-2026"
            }
        )

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(
            int(self.client.session["_auth_user_id"]),
            self.user.pk
        )

    def test_logout_requires_post(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("accounts:logout"))

        self.assertEqual(response.status_code, 405)
        self.assertIn("_auth_user_id", self.client.session)

    def test_user_can_logout_with_post(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("accounts:logout"))

        self.assertRedirects(response, reverse("home"))
        self.assertNotIn("_auth_user_id", self.client.session)


class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="profile-member",
            email="profile@example.com",
            password="A-strong-password-2026"
        )

    def test_public_profile_is_available_to_anonymous_users(self):
        response = self.client.get(
            reverse(
                "accounts:profile-detail",
                kwargs={"username": self.user.username}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_anonymous_user_cannot_edit_profile(self):
        response = self.client.get(reverse("accounts:profile-edit"))

        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next="
            f"{reverse('accounts:profile-edit')}"
        )

    def test_user_can_update_own_profile(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("accounts:profile-edit"),
            {
                "username": self.user.username,
                "email": "updated@example.com",
                "display_name": "Updated Member",
                "bio": "I collect excellent memes."
            }
        )

        self.assertRedirects(
            response,
            reverse(
                "accounts:profile-detail",
                kwargs={"username": self.user.username}
            )
        )

        self.user.refresh_from_db()
        self.assertEqual(self.user.display_name, "Updated Member")
        self.assertEqual(self.user.bio, "I collect excellent memes.")

    def test_username_cannot_be_changed_through_profile_form(self):
        self.client.force_login(self.user)

        self.client.post(
            reverse("accounts:profile-edit"),
            {
                "username": "tampered-name",
                "email": self.user.email,
                "display_name": self.user.display_name,
                "bio": self.user.bio
            }
        )

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "profile-member")