from django.db import models

# Create your models here.
class Posicion(models.Model):
    posicion = models.CharField(max_length=50)

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

class PosicionJugador(models.Model):
    posicion = models.ForeignKey(Posicion)
    jugador = models.ForeignKey(Jugador)

class Torneo(models.Model):
    torneo = models.CharField(max_length=50)

class Partido(models.Model):
    fecha = models.DateTimeField('fecha del partido')
    torneo = models.ForeignKey(Torneo)
    equipo1 = models.ForeignKey(Equipo, related_name='equipo1')
    equipo2 = models.ForeignKey(Equipo, related_name='equipo2')
    goles_equipo1 = models.IntegerField()
    goles_equipo2 = models.IntegerField()