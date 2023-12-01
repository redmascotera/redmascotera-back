"""
${name} tests
"""

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class ExampleTests(APITestCase):
    def test_test_api_view(self):
        url = reverse("example:test_api_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Hello, World!'})

    def test_class_based_api_view(self):
        url = reverse('example:test_class_based_api_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Hello, World!'})
