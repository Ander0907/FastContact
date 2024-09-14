from django.db import models

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(null=False)