from django.db import models


class identificacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100,
                                   null=True,
                                   blank=True)

