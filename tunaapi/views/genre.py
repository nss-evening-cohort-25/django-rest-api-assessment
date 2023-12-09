from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre, Song, SongGenre
from django.shortcuts import get_object_or_404


class GenreView(ViewSet):

    def retrieve(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
            serialized_data = GenreSerializer(genre)
            data = serialized_data.data
            data["songs"] = list()
            for song_genre in genre.genre_songs.all():
                song = song_genre.song
                song_serialized = SongSerializer(song)
                data["songs"].append(song_serialized.data)
            return Response(data)
        except Genre.DoesNotExist as ex:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        genres = Genre.objects.all()
        serialized_data = GenreSerializer(genres, many=True)
        return Response(serialized_data.data)

    def create(self, request):
        data = request.data
        genre = Genre.objects.create(
            description=data["description"],
        )
        serialized_data = GenreSerializer(genre)
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def destroy(self, _, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        data = request.data
        genre.description = data["description"]
        genre.save()
        serialiser = GenreSerializer(genre)

        return Response(serialiser.data, status=status.HTTP_200_OK)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'description')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', "length", "artist_id"]
