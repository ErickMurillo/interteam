# -*- coding: UTF-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from embed_video.fields import EmbedVideoField

# Create your models here.
class Tematica(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class GaleriaImagenes(models.Model):
	titulo = models.CharField(max_length=200)
	portada = ImageField(upload_to='galerias/')
	tematica = models.ForeignKey(Tematica,on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Galería imagenes'
		verbose_name_plural = 'Galerías imagenes'

class Imagenes(models.Model):
	imagenes = models.ForeignKey(GaleriaImagenes,on_delete=models.DO_NOTHING)
	nombre = models.CharField(max_length=200)
	imagen = ImageField(upload_to='galerias/')

############

class GaleriaVideos(models.Model):
	titulo = models.CharField(max_length=200)
	portada = ImageField(upload_to='galerias/')
	tematica = models.ForeignKey(Tematica,on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Galería videos'
		verbose_name_plural = 'Galerías videos'

class Videos(models.Model):
	video = models.ForeignKey(GaleriaVideos,on_delete=models.DO_NOTHING)
	titulo = models.CharField(max_length=200)
	url = EmbedVideoField()