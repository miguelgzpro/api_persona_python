from django.db import models

class TipoPersona(models.Model):
    descripcion = models.CharField(max_length=500)

class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    nro_identificacion = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    etnia = models.CharField(max_length=80)
    genero = models.CharField(max_length=80)
    estado_civil = models.CharField(max_length=80)
    TipoPersona = models.ForeignKey(TipoPersona, on_delete=models.PROTECT)

# otros modelos...
