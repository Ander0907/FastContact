# Generated by Django 5.0.2 on 2024-03-23 20:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0003_rename_task_reocrdatorio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reocrdatorio',
            new_name='Recordatorio',
        ),
    ]
