# Generated by Django 3.2.19 on 2023-06-05 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('nro_identificacion', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('etnia', models.CharField(max_length=80)),
                ('genero', models.CharField(max_length=80)),
                ('estado_civil', models.CharField(max_length=80)),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tipopersona')),
            ],
        ),
    ]
