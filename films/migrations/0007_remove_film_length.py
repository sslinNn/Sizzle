# Generated by Django 5.0.1 on 2024-01-11 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_film_genre_alter_film_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='length',
        ),
    ]