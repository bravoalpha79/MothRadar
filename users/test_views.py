from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import UserRegistrationForm, UserUpdateForm


class TestUserViews(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username="TestUser",
            email="test_email@example.com",
            password="testing123"
        )
        user1.save()
        self.tester = Client()

    def test_get_register_view(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")

    def test_profile_redirects_to_login_if_user_not_logged_in(self):
        response = self.client.get("/profile/")
        self.assertRedirects(response, "/login/?next=/profile/")

    def test_profile_update_redirects_to_login_if_user_not_logged_in(self):
        response = self.client.get("/profile/update/")
        self.assertRedirects(response, "/login/?next=/profile/update/")

    def test_get_profile(self):
        self.client.login(username="TestUser", password="testing123")
        response = self.client.get("/profile/")
        self.assertTemplateUsed("users/profile.html")

    def test_post_valid_registration_form(self):
        form = UserRegistrationForm(
            {
                "username": "TestUser2",
                "email": "test_email2@example.com",
                "password1": "testing456",
                "password2": "testing456",
            }
        )
        self.client.post("/register/")
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())
        form.save()
        new_user = get_object_or_404(User, username="TestUser2")
        self.assertTrue(new_user)

    def test_get_profile_update(self):
        self.tester.login(username="TestUser", password="testing123")
        response = self.tester.get("/profile/update/")
        self.assertTemplateUsed("users/profile_update.html")

    def test_post_valid_profile_update_form(self):
        self.tester.login(username="TestUser", password="testing123")
        user = get_object_or_404(User, username="TestUser")
        form = UserUpdateForm(
            {
                "username": "TestUser",
                "email": "test_email_changed@example.com"
            },
            instance=user,
        )
        self.tester.post("/profile/update/")
        self.assertTrue(form.is_valid())
        form.save()
        updated_user = get_object_or_404(User, username="TestUser")
        self.assertEqual(updated_user.email, "test_email_changed@example.com")
