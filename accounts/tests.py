from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(
            "user", "user@example.com", "password")
        user.save()

    def test_auth(self):
        url = reverse("auth")
        data = {"username": "user", "password": "password"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserTestCase(APITestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(
            "user", "user@example.com", "password")
        user.save()

        self.client.force_authenticate(
            user=user, token=user.auth_token)

    def test_create_user(self):
        url = reverse("user-list")
        data = {"username": "user2", "password": "password"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

