# animarte_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q 
from .models import Servicio, Animador, Resena
from .forms import ServicioForm, AnimadorForm, ResenaForm, BusquedaServicioForm

# 1. Vista de Listado / Home (Función)
def lista_servicios(request):
    servicios = Servicio.objects.all()
    form_busqueda = BusquedaServicioForm() 
    context = {
        'servicios': servicios,
        'form_busqueda': form_busqueda
    }
    return render(request, 'animarte_app/lista_servicios.html', context)

# 2. Vista de Búsqueda (Función)
def buscar_servicio(request):
    form = BusquedaServicioForm(request.GET or None)
    resultados = Servicio.objects.none() 
    termino = ''

    if form.is_valid():
        termino = form.cleaned_data.get('termino_busqueda')
        if termino:
            # Búsqueda por nombre O descripción (Q objects)
            resultados = Servicio.objects.filter(
                Q(nombre__icontains=termino) | Q(descripcion__icontains=termino)
            )

    context = {
        'form': form,
        'resultados': resultados,
        'termino': termino
    }
    return render(request, 'animarte_app/buscar_servicio.html', context)

# 3. Crear Servicio (Clase)
class CrearServicioView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'animarte_app/crear_registro.html' 
    success_url = reverse_lazy('lista_servicios') 

# 4. Crear Animador (Clase)
class CrearAnimadorView(CreateView):
    model = Animador
    form_class = AnimadorForm
    template_name = 'animarte_app/crear_registro.html' 
    success_url = reverse_lazy('lista_servicios') 

# 5. Crear Reseña (Clase)
class CrearResenaView(CreateView):
    model = Resena
    form_class = ResenaForm
    template_name = 'animarte_app/crear_registro.html' 
    success_url = reverse_lazy('lista_servicios')