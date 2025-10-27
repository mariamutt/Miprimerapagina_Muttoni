# animarte_app/admin.py

from django.contrib import admin
# Importa todos tus modelos
from .models import Servicio, Animador, Resena

# Registra cada modelo en el sitio de administración
admin.site.register(Servicio)
admin.site.register(Animador)
admin.site.register(Resena)