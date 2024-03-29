# Generated by Django 5.0.1 on 2024-01-26 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='cursos/')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='cursos/')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CaheUp.curso')),
            ],
        ),
    ]
