from django.conf.urls import url
from django.contrib import admin
from futbol.views import index, crear_equipo
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^equipos/$', crear_equipo, name='equipos')
]