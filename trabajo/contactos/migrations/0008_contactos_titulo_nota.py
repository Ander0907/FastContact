# Generated by Django 5.0.2 on 2024-03-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0007_remove_contactos_nota_remove_contactos_titulo_nota_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='titulo_nota',
            field=models.CharField(default='Sin titulo...', max_length=60, null=True),
        ),
    ]
