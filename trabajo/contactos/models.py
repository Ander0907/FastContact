from django.db import models

# Se define el modelo Contactos, que representa una tabla en la base de datos.
class Contactos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    empresa = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=15, null=False)
    direccion = models.CharField(max_length=60, null=True)
    titulo_nota = models.CharField(max_length=60, null=True, default='Sin titulo...')
    notas = models.TextField(null=True)
