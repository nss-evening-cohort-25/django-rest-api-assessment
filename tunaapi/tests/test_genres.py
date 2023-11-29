import unittest
from rest_framework.test import APIRequestFactory


class TestGenres(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = APIRequestFactory()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get("/customer/details/")