# Generated by Django 5.0.2 on 2024-03-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0005_delete_recordatorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactos',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='contactos',
            name='notas',
        ),
        migrations.AddField(
            model_name='contactos',
            name='nota',
            field=models.TextField(default='No hay nota'),
        ),
        migrations.AddField(
            model_name='contactos',
            name='titulo_nota',
            field=models.CharField(default='Sin título', max_length=20),
        ),
    ]
