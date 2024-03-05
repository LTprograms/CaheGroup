# Generated by Django 5.0.1 on 2024-02-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vicamar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='descuento',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='sub_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Cotizacion',
        ),
    ]
