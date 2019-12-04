# -*- coding: UTF-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.
class Proyecto(models.Model):
	nombre = models.CharField(max_length=300)
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	banner = ImageField(upload_to='informes/banner/',help_text='1350x500',blank=True,null=True)
	objectivos = RichTextUploadingField()
	descripcion = RichTextUploadingField()
	imagen_descripcion = ImageField(upload_to='informes/img-descripcion/',help_text='800x600',blank=True,null=True)
	coordinador_proyecto = models.CharField(max_length=300,verbose_name='Coordinador general del proyecto')
	email = models.EmailField()
	celular = models.CharField(max_length=50)
	responsable_proyecto = models.CharField(max_length=300)
	slug = models.SlugField(max_length=320,editable=False)
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	url_para_compartir = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		self.url_para_compartir = 'https://cluster-nicaragua.net/informes/' + self.slug
		return super(Proyecto, self).save(*args, **kwargs)

class Archivo(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=300)
	archivo = models.FileField(upload_to='informes/archivos/')

	class Meta:
		verbose_name = 'Archivo proyecto'
		verbose_name_plural = 'Archivos proyecto'

REPORTE_CHOICES = (('Informe técnico','Informe técnico'),('Informe financiero','Informe financiero'))

class Informe(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	tipo_reporte = models.CharField(max_length=50,choices=REPORTE_CHOICES)
	inicio = models.DateField()
	fin = models.DateField()
	fecha_informe = models.DateField()
	# nombre = models.CharField(max_length=300)
	archivo = models.FileField(upload_to='informes/informe/')

class RangoFechaImagenes(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	inicio = models.DateField()
	fin = models.DateField()

	class Meta:
		verbose_name = 'Fecha Imágen'
		verbose_name_plural = 'Fecha Imágenes'

class Imagenes(models.Model):
	rango = models.ForeignKey(RangoFechaImagenes,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=300)
	archivo = ImageField(upload_to='informes/imgenes/')

	class Meta:
		verbose_name = 'Imágen'
		verbose_name_plural = 'Imágenes'

class Video(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=300)
	url = EmbedVideoField()

class Documento(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=300)
	descripcion = models.TextField()
	imagen = ImageField(upload_to='informes/imgenes/',null=True, blank=True)
	archivo = models.FileField(upload_to='informes/documentos/')

class HistoriasExito(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)
	foto = ImageField(upload_to='informes/historias-exito/',null=True, blank=True)
	texto = models.TextField()

	class Meta:
		verbose_name = 'Historia de éxito'
		verbose_name_plural = 'Historias de éxito'

class Monitoreo(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)
	foto = ImageField(upload_to='informes/monitoreo/',null=True, blank=True)

	class Meta:
		verbose_name = 'Anexo'
		verbose_name_plural = 'Anexos'

class ArchivosMonitoreo(models.Model):
	monitoreo = models.ForeignKey(Monitoreo,on_delete=models.CASCADE)
	archivo = models.FileField(upload_to='informes/monitoreo/')

	class Meta:
		verbose_name = 'Archivo'
		verbose_name_plural = 'Archivos'