"""
Import json data from URL to Datababse
"""
import requests
import json
from hPlay.models import Song
from django.core.management.base import BaseCommand
from datetime import datetime

IMPORT_URL = 'http://starlord.hackerearth.com/studio'

#imports song details from the above url
class Command(BaseCommand):
    def import_Song(self, data):
        song = data.get('song', None)
        url = data.get('url', None)
        artists = data.get('artists',None)
        cover_image = data.get('cover_image',None)

        try:
            songs, created = Song.objects.get_or_create(
                song=song,
                url=url,
                artists=artists,
                cover_image=cover_image
            )
            if created:
                songs.save()
                display_format = "\nSong, {}, has been saved."
                print(display_format.format(songs))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this song: {}\n{}".format(title, str(ex))
            print(msg)


    def handle(self, *args, **options):
        """
        Makes a GET request to the  API.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )

        response.raise_for_status()
        data = response.json()

        for data_object in data:
            self.import_Song(data_object)
