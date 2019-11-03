from django.contrib import admin
from hPlay.models import Song
from django.core import management
from django.shortcuts import redirect

#adds the list of songs in django admin when imported from url
class SongAdmin(admin.ModelAdmin):
    @admin.site.register_view('import_song_from_url', 'Import Songs from URL')
    def import_song_from_url(request):
        print('import songs here')
        try:
            management.call_command('import_from_url')
            message = 'successfully imported data from URL'

        except Exception as ex:
            message = 'Error importing from data from URL {}'.format(str(ex))

            admin.ModelAdmin.message_user(Song, request, message)
            return redirect('admin:index')

admin.site.register(Song, SongAdmin)
