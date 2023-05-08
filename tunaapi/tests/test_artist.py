import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tunaapi.models import Artist
from tunaapi.views.artist_view import ArtistSerializer


class ArtistTests(APITestCase):

    def setUp(self) -> None:
        Artist.objects.create(name='John Q. Public', bio='Nobody', age=19)

    def test_list_artists(self) -> None:
        """Test list artists"""
        url = reverse('artist-list')

        response = self.client.get(url)

        # Get all the artists in the database and serialize them to get the expected output
        all_artists = Artist.objects.all()
        expected = ArtistSerializer(all_artists, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_create_artist(self) -> None:
        """Test creating a new artist"""
        url = reverse('artist-list')

        # POST new artist and get JSON response
        artist = {
            "bio": "Veniam voluptatem vero dolorem consequuntur quia.",
            "age": 25,
            "name": "Olivia Vanderheuk"
        }
        response = self.client.post(url, artist, format='json')
        response_json = json.loads(response.content)

        # Assert correct status code and values
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response_json["bio"], "Veniam voluptatem vero dolorem consequuntur quia.")
        self.assertEqual(response_json["age"], 25)
        self.assertEqual(response_json["name"], "Olivia Vanderheuk")
        self.assertIn('id', response_json)

    def test_get_404_artist(self) -> None:
        """Get non-existant single artist test"""
        url = reverse('artist-detail', args=[1003])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_single_artist(self) -> None:
        """Get single artist test"""
        artist_to_test = Artist.objects.first()
        url = reverse('artist-detail', args=[artist_to_test.id])

        response = self.client.get(url)
        response_json = json.loads(response.content)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response_json["bio"], "Nobody")
        self.assertEqual(response_json["age"], 19)
        self.assertEqual(response_json["name"], "John Q. Public")
        self.assertIn('id', response_json)
