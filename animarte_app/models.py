# animarte_app/models.py

from django.db import models

# Modelo 1: Servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    edad_minima = models.IntegerField()
    duracion = models.CharField(max_length=50, help_text="Ej: 2 horas, 90 minutos")

    def __str__(self):
        return self.nombre

# Modelo 2: Animador
class Animador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True) 
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo 3: Resena (Clave Foránea a Servicio) - ¡Clase corregida!
class Resena(models.Model):
    # ¡related_name corregido!
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='resenas') 
    nombre_cliente = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 

    def __str__(self):
        # ¡Usamos Reseña en el string para la presentación, pero Resena en el código!
        return f"Reseña de {self.nombre_cliente} para {self.servicio.nombre}"