from django.db import models

class Song(models.Model):
    song = models.CharField(default='', max_length=1000)
    url = models.CharField(default='', max_length=1000)
    artists = models.CharField(default='', max_length=1000)
    cover_image = models.CharField(default='', max_length=1000)

    def __str__(self):
        return self.song
