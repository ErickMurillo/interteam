# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from contrapartes.models import Departamento

# Create your models here.
class TipoProducto(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Tipos de Productos"
		verbose_name = "Tipo de Producto"

class ServiciosProducto(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Servicios de Productos"
		verbose_name = "Servicio de Producto"

class Producto(models.Model):
	nombre = models.CharField(max_length=250)
	descripcion = RichTextUploadingField()
	precio = models.CharField(max_length=250,verbose_name='Precio y unidad de medida',blank=True,null=True)
	foto_principal = ImageField(upload_to='productos/')
	tipo_producto = models.ManyToManyField(TipoProducto,blank=True)
	tipo_servicio = models.ManyToManyField(ServiciosProducto,blank=True)
	localizacion = models.ManyToManyField(Departamento)
	disponible = models.BooleanField()
	publicada = models.BooleanField()
	enviar_correo = models.BooleanField()
	correo_enviado = models.BooleanField(editable=False)
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	contacto_1 = models.CharField(max_length=200,blank=True, null=True)
	correo_1 = models.EmailField(blank=True, null=True)
	telefono_1 = models.CharField(max_length=200, blank=True, null=True)
	contacto_2 = models.CharField(max_length=200,blank=True, null=True)
	correo_2 = models.EmailField(blank=True, null=True)
	telefono_2 = models.CharField(max_length=200, blank=True, null=True)
	vistas = models.IntegerField(editable=False,default=0)
	slug = models.SlugField(max_length=250,editable=False)

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		return super(Producto, self).save(*args, **kwargs)

class Propuesta_valor(models.Model):
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
	texto = models.CharField(max_length=300)

	class Meta:
		verbose_name_plural = "Propuesta de valor"
		verbose_name = "Propuesta de valor"

class FotosProducto(models.Model):
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
	foto = ImageField(upload_to='productos/')

	class Meta:
		verbose_name_plural = "Fotos"
		verbose_name = "Foto"

class ArchivosProducto(models.Model):
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	archivo = models.FileField(upload_to='producto/archivos/')

	class Meta:
		verbose_name_plural = "Archivos"
		verbose_name = "Archivo"

REDES_CHOICES = (('Sitio web','Sitio web'),('Facebook','Facebook'),('Twitter','Twitter'),('Youtube','Youtube'),
					('Google+','Google+'),('Instagram','Instagram'),('Linkedin','Linkedin'),
					('Flickr','Flickr'),('Pinterest','Pinterest'),('Vimeo','Vimeo'),('Otra','Otra'),)

class Redes(models.Model):
	producto = models.ForeignKey(Producto,on_delete=models.DO_NOTHING)
	opcion = models.CharField(max_length=25,choices=REDES_CHOICES)
	url = models.URLField()

	class Meta:
		verbose_name = 'Red'
		verbose_name_plural = 'Redes'
