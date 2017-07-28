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