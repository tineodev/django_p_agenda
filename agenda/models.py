from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return  f"{self.nombre} {self.apellido} - {self.telefono}"


