from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from notas.models import *
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

# Create your models here.
class Informacion(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Información'

class Herramientas(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Herramientas'

class Publicacion(models.Model):
	titulo = models.CharField(max_length=250)
	imagen = ImageField(upload_to='publicaciones/img/',null=True, blank=True,help_text='Tamaño recomendado: 360x390')
	# archivo = models.FileField(upload_to='publicaciones/archivos/')
	resumen = RichTextUploadingField()
	tematica = models.ForeignKey(Temas,on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	slug = models.SlugField(max_length=250,editable=False)
	publicada = models.BooleanField()
	correo_enviado = models.BooleanField(editable=False, null=True)
	informacion = models.ForeignKey(Informacion,on_delete=models.DO_NOTHING,null=True, blank=True)
	herramienta = models.ForeignKey(Herramientas,on_delete=models.DO_NOTHING,null=True, blank=True)

	def __str__(self):
		return u'%s' % self.titulo

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Publicacion, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Biblioteca'
		verbose_name = 'Biblioteca'

class ArchivosPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	archivo_pdf = models.FileField(upload_to='publicaciones/archivos/')

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Archivos'

class AudiosPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	archivo_audio = models.FileField(upload_to='publicaciones/audios/')

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Audios'

class VideosPublicacion(models.Model):
	publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=250)
	url = models.URLField()

	def __str__(self):
		return u'%s' % self.nombre

	class Meta:
		verbose_name_plural = 'Videos'
