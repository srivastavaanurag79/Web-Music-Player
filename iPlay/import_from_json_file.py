"""
Import json data from JSON file to Datababse
"""
import os
import io
import json
from import_data.models import Song
from django.core.management.base import BaseCommand
from datetime import datetime
from data_import.settings import BASE_DIR


class Command(BaseCommand):
    def import_song_from_file(self):
        data_folder = os.path.join(BASE_DIR, 'import_data', 'studio')
        for data_file in os.listdir(data_folder):
            with io.open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    song = data_object.get('song', None)
                    url = data_object.get('url', None)
                    artists = data.object.get('artists',None)
                    cover_image = data.object.get('cover_image',None)

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
                            print(display_format.format(song))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this song: {}\n{}".format(title, str(ex))
                        print(msg)


    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_song_from_file()
