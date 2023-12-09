from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Genre, Artist
from django.shortcuts import get_object_or_404

class SongView(ViewSet):

    def retrieve(self, request, pk):
        try:
            song = Song.objects.get(pk=pk)
            serialized_data = SongArtistSerializer(song)
            data = serialized_data.data
            data["genres"] = list()
            for song_genre in song.song_genres.all():
                genre = song_genre.genre
                print(genre)
                genre_serialized = GenreSerializer(genre)
                data["genres"].append(genre_serialized.data)
            return Response(data)
        except Song.DoesNotExist as ex:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        songs = Song.objects.all()
        serialized_data = SongSerializer(songs, many=True)
        return Response(serialized_data.data)

    def create(self, request):
        data = request.data
        artist = Artist.objects.get(pk=data["artist_id"])
        genre = Song.objects.create(
            title=data["title"],
            artist=artist,
            album=data["album"],
            length=data["length"],
        )
        serialized_data = SongSerializer(genre)
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def destroy(self, _, pk):
        genre = get_object_or_404(Song, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        data = request.data
        song.title = data["title"]
        song.artist = Artist.objects.get(pk=data["artist_id"])
        song.album = data["album"]
        song.length = data["length"]
        song.save()

        serializer = SongSerializer(song)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'description')


class SongArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', "length", "artist"]
        depth = 1
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', "length", "artist_id"]
