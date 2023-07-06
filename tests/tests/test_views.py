from django.test import TestCase
from rest_framework import status

from .. import models


class TestSelectorAPIView(TestCase):
    def test(self):
        models.Item.objects.create(name="ASD", size=45)
        expected_response = [{"name": "ASD", "size": 45}]

        response = self.client.get("/api/items/")

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_response, response.json())
