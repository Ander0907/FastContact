# Generated by Django 5.0.2 on 2024-03-23 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0004_rename_reocrdatorio_recordatorio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recordatorio',
        ),
    ]
