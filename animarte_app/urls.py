# animarte_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 1. Listado / Home (La ruta raíz)
    path('', views.lista_servicios, name='lista_servicios'), 
    
    # 2. Búsqueda
    path('buscar/', views.buscar_servicio, name='buscar_servicio'),
    
    # 3. Crear Servicio
    path('servicio/crear/', views.CrearServicioView.as_view(), name='crear_servicio'),
    
    # 4. Crear Animador
    path('animador/crear/', views.CrearAnimadorView.as_view(), name='crear_animador'),
    
    # 5. Crear Reseña (usando resena sin ñ)
    path('resena/crear/', views.CrearResenaView.as_view(), name='crear_resena'),
]