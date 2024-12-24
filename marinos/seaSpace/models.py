from django.db import models

# Create your models here.
''' class  Marinos(models.Model):
    cedula = models.CharField(max_length =12, verbose_name="Cedula", null=False,blank=False, primary_key=True)
    nombres = models.CharField(max_length =40, verbose_name="Nombres")
    apellidos = models.CharField(max_length =40, verbose_name="Apellidos")
    fechaNacimiento= models.DateField(verbose_name="Fecha de Nacimiento")
    fechaControl= models.DateField(verbose_name="Fecha de Nacimiento")

class certificadoMarino(models.Model):
    registro= models.IntegerField()
    cedulaMarino = models.CharField(verbose_name="Cedula Marino", null=False,blank=False, max_length=12)
    idDocumento = models.IntegerField(verbose_name="Tipo de Documento")
    fechaExpedicion = models.DateField(verbose_name="Fecha de Expedición Documento")
    fechavencimiento= models.DateField(verbose_name="Fecha de vencimiento Documento")
    fechaControl= models.DateField()

class catalogoDocumetosMarinos(models.Model):
    idDocumento= models.IntegerField()
    nombreDocumento= models.CharField(max_length= 60,verbose_name="Nombre del Documento")
    codigoGeneralDocumento = models.CharField(max_length=50, verbose_name="Código o Nobre Internacional del Documento")
    
'''