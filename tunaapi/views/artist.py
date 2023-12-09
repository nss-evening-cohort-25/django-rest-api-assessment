from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from django.db.models import Count

from tunaapi.models import Artist, Song


class ArtistView(ViewSet):

    def retrieve(self, request, pk):
        try:
            artist = Artist.objects.annotate(song_count=Count('songs')).get(pk=pk)
            serialized_data = ArtistSongSerializer(artist)
            return Response(serialized_data.data)
        except Artist.DoesNotExist as ex:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        artists = Artist.objects.all()
        serialized_data = ArtistSerializer(artists, many=True)
        return Response(serialized_data.data)

    def create(self, request):
        data = request.data
        artist = Artist.objects.create(
            name=data["name"],
            age=data["age"],
            bio=data["bio"]
        )
        serialized_data = ArtistSerializer(artist)
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        artist = get_object_or_404(Artist, pk=pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        artist = get_object_or_404(Artist, pk=pk)
        data = request.data
        artist.name = data["name"]
        artist.age = data["age"]
        artist.bio = data["bio"]
        artist.save()

        ser = ArtistSerializer(artist)

        return Response(ser.data, status=status.HTTP_200_OK)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', "age", "bio")
        depth = 1


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', "length"]

class ArtistSongSerializer(serializers.ModelSerializer):
    song_count = serializers.IntegerField(default=None)
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', "age", "bio", "songs", "song_count")
