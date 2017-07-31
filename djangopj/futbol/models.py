from django.db import models


# Create your models here.
class Posicion(models.Model):
    posicion = models.CharField(max_length=50)

class Equipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)

class PosicionJugador(models.Model):
    posicion = models.ForeignKey(Posicion)
    jugador = models.ForeignKey(Jugador)

class Torneo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __puntos(equipo):
        partidos = Partido.objects.filter(models.Q(equipo1 = equipo) | models.Q(equipo2 = equipo))
        goles_favor = goles_contra = puntos = 0
        for partido in partidos:
            if (partido.equipo1 == equipo):
                goles_favor += partido.goles_equipo1
                goles_contra += partido.goles_equipo2
                if (partido.goles_equipo1 > partido.goles_equipo2):
                    puntos += 3
                elif (partido.goles_equipo1 == partido.goles_equipo2):
                    puntos += 1
            else:
                goles_favor += partido.goles_equipo2
                goles_contra += partido.goles_equipo1
                if (partido.goles_equipo2 > partido.goles_equipo1):
                    puntos += 3
                elif (partido.goles_equipo1 == partido.goles_equipo2):
                    puntos += 1

        return {'nombre': equipo.nombre, 'goles_favor': goles_favor, 'goles_contra': goles_contra, 'puntos': puntos }

    def tabla(torneo):
        equipos = Equipo.objects.all()
        torneo=[]
        for equipo in equipos:
            torneo.append(Torneo.__puntos(equipo))
        return torneo



class Partido(models.Model):
    fecha = models.DateTimeField('fecha del partido')
    torneo = models.ForeignKey(Torneo)
    equipo1 = models.ForeignKey(Equipo, related_name='equipo1')
    equipo2 = models.ForeignKey(Equipo, related_name='equipo2')
    goles_equipo1 = models.IntegerField()
    goles_equipo2 = models.IntegerField()





