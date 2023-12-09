from django.db import models
from . import Song, Genre

class SongGenre(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="song_genres")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genre_songs")
