from django.conf.urls import url
from django.contrib import admin
from futbol.views import index, crear_equipo, jugadores, torneos
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^equipos/$', crear_equipo, name='equipos'),
    url(r'^jugadores/$', jugadores, name='jugadores'),
    url(r'^torneos/$', torneos, name='torneos')
]