import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tunaapi.models import Song, Artist, Genre
from tunaapi.views.song_view import SongSerializer


class SongTests(APITestCase):

    def setUp(self) -> None:
        john = Artist.objects.create(name='John Q. Public', bio='Nobody', age=19)
        pop = Genre.objects.create(description='Pop')

        Song.objects.create(
            title='First Song',
            album='First Album',
            length=256,
            artist=john,
            genre=pop
        )

    def test_list_songs(self) -> None:
        """Test list songs"""
        url = reverse('song-list')

        response = self.client.get(url)

        # Get all the songs in the database and serialize them to get the expected output
        all_songs = Song.objects.all()
        expected = SongSerializer(all_songs, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_create_song(self) -> None:
        """Test creating a new song"""
        url = reverse('song-list')

        artist = Artist.objects.first()
        genre = Genre.objects.first()

        # POST new song and get JSON response
        song = {
            "title": "Second Song",
            "length": 341,
            "album": "Second Album",
            "genreId": genre.id,
            "artistId": artist.id
        }
        response = self.client.post(url, song, format='json')
        response_json = json.loads(response.content)

        # Assert correct status code and values
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response_json["title"], "Second Song")
        self.assertEqual(response_json["album"], "Second Album")
        self.assertEqual(response_json["length"], 341)
        self.assertIn('id', response_json)

    def test_get_404_song(self) -> None:
        """Get non-existant single song test"""
        url = reverse('song-detail', args=[1003])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_single_song(self) -> None:
        """Get single song test"""
        song_to_test = Song.objects.first()
        url = reverse('song-detail', args=[song_to_test.id])

        response = self.client.get(url)
        response_json = json.loads(response.content)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertIn('id', response_json)
        self.assertEqual(response_json["title"], "First Song")
        self.assertEqual(response_json["length"], 256)
        self.assertEqual(response_json["album"], "First Album")

        self.assertIn('artist', response_json)
        self.assertIn('name', response_json["artist"])
        self.assertEqual(response_json["artist"]["name"], "John Q. Public")

        self.assertIn('genre', response_json)
        self.assertIn('description', response_json["genre"])
        self.assertEqual(response_json["genre"]["description"], "Pop")
