from operator import mod
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=250)
    def __str__(self):
        return self.nombre
    
