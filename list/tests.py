from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from list.models import List, Item

class ListTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="admin", password="test")
        cls.list1 = List.objects.create(name="test",owner=cls.user1)

    def test_create(self):
        self.client.force_authenticate(self.user1)
        url = reverse('list-list')
        data = {"name": "test"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["name"], "test")
        self.assertEqual(response.data["owner"], self.user1.id)

    def test_get(self):
        self.client.force_authenticate(self.user1)
        url = reverse('list-detail', kwargs={'pk':self.list1.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.data["name"], "test")
        self.assertEqual(response.data["owner"], self.user1.id)

class ItemTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="admin", password="test")
        cls.list1 = List.objects.create(name="test", owner=cls.user1)

    def test_create(self):
        self.client.force_authenticate(self.user1)
        url = reverse('item-list')
        data = {"list_id": self.list1.id, "text": "test"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["text"], "test")
        self.assertEqual(response.data["list"], self.list1.id)