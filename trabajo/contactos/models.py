from django.db import models  # Importa el módulo de modelos de Django, que proporciona clases para definir la estructura de la base de datos.

# Se define el modelo Contactos, que representa una tabla en la base de datos.
class Contactos(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de clave primaria que se autoincrementa automáticamente.
    nombre = models.CharField(max_length=30, null=False)  # Campo para almacenar el nombre del contacto, de tipo CharField con longitud máxima de 30 caracteres, no puede ser nulo.
    empresa = models.CharField(max_length=30, null=False)  # Campo para almacenar el nombre de la empresa del contacto, de tipo CharField con longitud máxima de 30 caracteres, no puede ser nulo.
    correo = models.CharField(max_length=50, null=False)  # Campo para almacenar el correo del contacto, de tipo CharField con longitud máxima de 50 caracteres, no puede ser nulo.
    telefono = models.CharField(max_length=15, null=False)  # Campo para almacenar el número de teléfono del contacto, de tipo CharField con longitud máxima de 15 caracteres, no puede ser nulo.
    direccion = models.CharField(max_length=60, null=True)  # Campo para almacenar la dirección del contacto, de tipo CharField con longitud máxima de 60 caracteres, puede ser nulo.
    titulo_nota = models.CharField(max_length=60, null=True, default='Sin titulo...')  # Campo para almacenar el título de la nota del contacto, de tipo CharField con longitud máxima de 60 caracteres, puede ser nulo, con un valor predeterminado 'Sin titulo...'.
    notas = models.TextField(null=True)  # Campo para almacenar las notas del contacto, de tipo TextField, puede ser nulo.
