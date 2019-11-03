from django.shortcuts import render

from hPlay.models import Song

#the base html file
def index(request):
    songs = Song.objects.all()
    return render(request, 'hPlay/base.html', context={
        'playlist': songs})

#displayes the list of songs
def songs(request):
    songs = Song.objects.all().order_by('artists')
    cover = 'posters/cover arts/All.jpg'
    return render(request, 'hPlay/content_page.html',
                  context={'playlist': songs, 'cover': cover})

#error
def error_404(request):
    return render(request, 'hPlay/content_page.html', context={'errors': True})
