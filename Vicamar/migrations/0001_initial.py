# Generated by Django 5.0.1 on 2024-02-02 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('razon_social', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
                ('precio', models.FloatField()),
                ('modelo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('fin', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vicamar.cliente')),
                ('maquinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vicamar.maquinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('descuento', models.FloatField()),
                ('sub_total', models.FloatField()),
                ('alquiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vicamar.alquiler')),
            ],
        ),
    ]
