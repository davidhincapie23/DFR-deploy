from django.db import models

# Create your models here.

class Desarrollador(models.Model):
    nombre = models.CharField( max_length=50)
    años_de_exp =  models.IntegerField()
    lenguaje = models.CharField( max_length=50)
    framework = models.CharField( max_length=50)


    