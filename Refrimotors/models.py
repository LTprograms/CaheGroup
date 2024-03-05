from django.db import models

# Create your models here.
class Area(models.Model):
    area = models.CharField(max_length=30)

class TipoServicio(models.Model):
    tipo = models.CharField(max_length=30)

class Trabajador(models.Model):
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    cargo = models.CharField(max_length=30)
    jefe = models.ForeignKey('Refrimotors.Trabajador', on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

class Cliente(models.Model):
    ruc = models.CharField(max_length=15)
    razon_social = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    domicilio_fiscal = models.CharField(max_length=100)
    distrito = models.CharField(max_length=30)

class Sede(models.Model):
    sede = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Edificio(models.Model):
    edificio = models.CharField(max_length=30)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Piso(models.Model):
    piso = models.CharField(max_length=30)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

class TipoEquipo(models.Model):
    tipo = models.CharField(max_length=30)    

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    estado = models.BooleanField()
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE)

class LineaNegocio(models.Model):
    linea = models.CharField(max_length=50)

class Negocio(models.Model):
    negocio = models.CharField(max_length=50)
    linea = models.ForeignKey(LineaNegocio, on_delete = models.CASCADE)

class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=50)

class Solicitud(models.Model):
    documento = models.FileField(upload_to='solicitudes/')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField()
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)

class Servicio(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    limpieza = models.BooleanField()
    inspeccion = models.BooleanField()
    lubricacion = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)    
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)

