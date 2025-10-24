from django import forms
# Importamos el modelo Resena (sin ñ)
from .models import Servicio, Animador, Resena

# --- Formularios de Inserción (ModelForm) ---

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        # Incluye todos los campos excepto el 'id'
        fields = ['nombre', 'descripcion', 'precio', 'edad_minima', 'duracion'] 

class AnimadorForm(forms.ModelForm):
    class Meta:
        model = Animador
        fields = ['nombre', 'apellido', 'rut', 'especialidad', 'telefono']

# Formulario para el modelo Resena (sin ñ)
class ResenaForm(forms.ModelForm):
    class Meta:
        # Usamos el modelo corregido: Resena
        model = Resena
        # Incluye el FK 'servicio' para asociar la reseña
        fields = ['servicio', 'nombre_cliente', 'comentario', 'puntuacion'] 

# --- Formulario de Búsqueda (Form simple) ---

class BusquedaServicioForm(forms.Form):
    termino_busqueda = forms.CharField(
        max_length=100, 
        required=False,
        label='Buscar Servicios',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre o descripción del servicio'})
    )