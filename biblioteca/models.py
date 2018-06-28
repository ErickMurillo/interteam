from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from notas.models import *

# Create your models here.
class Archivos(models.Model):
	titulo = models.CharField(max_length=250)
	imagen = ImageField(upload_to='biblioteca/img/',null=True, blank=True)
	autor = models.CharField(max_length=250)
	editorial = models.CharField(max_length=250)
	lugar = models.CharField(max_length=250)
	fecha_publicacion = models.DateField()
	isbn = models.CharField(max_length=250,null=True,blank=True)
	numero_paginas = models.IntegerField()
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	resumen = RichTextUploadingField()
	archivo = models.FileField(upload_to='biblioteca/archivos/')
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,editable=False)
	slug = models.SlugField(max_length=300,editable=False)

	def __str__(self):
		return u'%s' % self.titulo

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Archivos, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Archivos'