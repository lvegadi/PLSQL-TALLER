from django.db import models
from django.conf import settings

# Create your models here.
class Alumno (models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField( blank=True, null=True)
    activo = models.CharField(max_length=1,default=1)

class Asignatura (models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.CharField(max_length=1,default=1);

class Nota (models.Model):    
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    ano = models.DecimalField(max_digits=4,decimal_places=0,default=2022)
    n1 = models.DecimalField(max_digits=4, decimal_places=2)
    n2 = models.DecimalField(max_digits=4, decimal_places=2)
    n3 = models.DecimalField(max_digits=4, decimal_places=2)
    activo = models.CharField(max_length=1,default=1);
   

User = settings.AUTH_USER_MODEL

class Auditoria (models.Model):
    accion = models.CharField(max_length=15)
    campo = models.CharField(max_length=15)
    valor_old = models.CharField(max_length=200)
    valor_new = models.CharField(max_length=200)
    fecha = models.DateTimeField( blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)