from django import forms
from futbol.models import *

class EquipoForm(forms.ModelForm):
    nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'})
    )
    class Meta:
        model = Equipo
        fields = ['nombre']

class JugadorForm(forms.ModelForm):
    nombre = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control', 'ng-model': 'nuevoJugador.nombre'}))
    apellido = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control', 'ng-model': 'nuevoJugador.apellido'}))
    dni = forms.IntegerField(
        required=True,
        widget = forms.TextInput(attrs={'placeholder': 'DNI', 'class': 'form-control', 'ng-model': 'nuevoJugador.dni'}))
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all(),
        required=True,
        widget = forms.Select(attrs={'class': 'form-control', 'ng-model': 'nuevoJugador.equipo'}))
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'dni', 'equipo']
