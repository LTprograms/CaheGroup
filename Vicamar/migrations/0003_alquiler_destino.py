# Generated by Django 5.0.1 on 2024-02-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vicamar', '0002_alquiler_cantidad_alquiler_descuento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='destino',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
