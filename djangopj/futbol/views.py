from django.shortcuts import render, redirect
from futbol.form import EquipoForm

def index(request):
    return render(request, 'futbol/index.html')

def crear_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos')
    else:
        form = EquipoForm()
    return render(request, 'futbol/crear_equipo.html', {'form': form})