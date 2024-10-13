from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre= models.CharField(max_length=100)
    apPaterno=models.CharField(max_length=100)
    apMaterno=models.CharField(max_length=100)