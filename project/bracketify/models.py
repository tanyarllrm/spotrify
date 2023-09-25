import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Record(models.Model):
    artist_name = models.CharField(max_length=128)
    album_name = models.CharField(max_length=128)
    song_name = models.CharField(max_length=128)
    user = models.CharField(max_length=32)
    ranking = models.IntegerField()

    def __str__(self):
        return f"{self.user} Ranking for {self.artist_name} - {self.song_name}: {self.ranking}"


# class Song(models.Model):
#     name = models.CharField(max_length=128)
#     id = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name
