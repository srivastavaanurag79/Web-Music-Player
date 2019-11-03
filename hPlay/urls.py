from django.conf.urls import url
from hPlay import views

app_name = 'hPlay'
urlpatterns = [
    url(r'^$', views.index, name='Homepage'),
    url(r'^songs', views.songs, name='Songs'),
    url(r'^404/', views.error_404, name="404")
]
