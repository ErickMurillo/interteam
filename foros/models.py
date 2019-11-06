# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
# from south.modelsinspector import add_introspection_rules
# from tagging.models import Tag
# from tagging_autocomplete.models import TagAutocompleteField
from taggit_autosuggest.managers import TaggableManager
from django.contrib.auth.models import User
#from contrapartes.models import Usuarios
# from thumbs import ImageWithThumbsField
from sorl.thumbnail import ImageField
from utils import *
import datetime
# from south.modelsinspector import add_introspection_rules
from ckeditor_uploader.fields import RichTextUploadingField

# add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])
# add_introspection_rules ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"])

# Create your models here.

class Imagen(models.Model):
	''' Modelo generico para subir imagenes en todos los demas app :)'''
	content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
	object_id = models.IntegerField(db_index=True)
	content_object = fields.GenericForeignKey('content_type', 'object_id')

	nombre_img = models.CharField("Nombre",max_length=200, null=True, blank=True)
	foto = ImageField("Foto",upload_to=get_file_path,null=True, blank=True)
	tags_img = TaggableManager("Tags",help_text='Separar elementos con "," ', blank=True)
	fileDir = 'fotos/'
	class Meta:
		verbose_name_plural = "Imágenes"

	def __str__(self):
		return self.nombre_img

class Documentos(models.Model):
	''' Modelo generico para subir los documentos en distintos app'''
	content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
	object_id = models.IntegerField(db_index=True)
	content_object = fields.GenericForeignKey('content_type', 'object_id')

	nombre_doc = models.CharField("Nombre",max_length=200, null=True, blank=True)
	adjunto = models.FileField("Adjunto",upload_to=get_file_path, null=True, blank=True)
	tags_doc = TaggableManager("Tags",help_text='Separar elementos con "," ', blank=True)

	fileDir = 'documentos/'

	class Meta:
		verbose_name_plural = "Documentos"

	def __str__(self):
		return self.nombre_doc

class Videos(models.Model):
	''' Modelo generico para subir videos en todos los app'''
	content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
	object_id = models.IntegerField(db_index=True)
	content_object = fields.GenericForeignKey('content_type', 'object_id')

	nombre_video = models.CharField(max_length=200, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	tags_vid = TaggableManager(help_text='Separar elementos con "," ', blank=True)

	class Meta:
		verbose_name_plural = "Videos"

	def __str__(self):
		return self.nombre_video

class Audios(models.Model):
	'''' Modelo generico para subir audios en todos los demas app '''
	content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
	object_id = models.IntegerField(db_index=True)
	content_object = fields.GenericForeignKey('content_type', 'object_id')

	nombre_audio = models.CharField(max_length=200, null=True, blank=True)
	audio = models.FileField(upload_to=get_file_path, null=True, blank=True)
	tags_aud = TaggableManager(help_text='Separar elementos con "," ', blank=True)

	fileDir = 'audios/'

	class Meta:
		verbose_name_plural = "Audios"

	def __str__(self):
		return self.nombre_audio

class Foros(models.Model):
	nombre = models.CharField(max_length=200)
	creacion = models.DateField(auto_now_add=True)
	apertura = models.DateField('Apertura y recepción de aportes')
	cierre = models.DateField('Cierre de aportes')
	fecha_skype = models.DateField('Propuesta de reunión skype')
	memoria = models.DateField('Propuesta entrega de memoria')
	contenido = RichTextUploadingField()
	contraparte = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	#documentos = fields.GenericRelation(Documentos)
	#fotos = fields.GenericRelation(Imagen)
	#video = fields.GenericRelation(Videos)
	#audio = fields.GenericRelation(Audios)
	correo_enviado = models.BooleanField(editable=False)

	class Meta:
		verbose_name_plural = "Foros"
		ordering = ['-creacion']

	def __str__(self):
		return self.nombre

	def __documento__(self):
		lista = []
		for obj in self.documentos.all():
			lista.append(obj)
		return lista

	def __fotos__(self):
		lista = []
		for obj in self.fotos.all():
			lista.append(obj)
		return lista

	def __video__(self):
		lista = []
		for obj in self.video.all():
			lista.append(obj)
		return lista

	def __audio__(self):
		lista = []
		for obj in self.audio.all():
			lista.append(obj)
		return lista

	def get_absolute_url(self):
		return "/foros/ver/%d" % (self.id)

class Aportes(models.Model):
	foro = models.ForeignKey(Foros,on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)
	contenido = RichTextUploadingField()
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	adjuntos = fields.GenericRelation(Documentos)
	fotos = fields.GenericRelation(Imagen)
	video = fields.GenericRelation(Videos)
	audio = fields.GenericRelation(Audios)

	class Meta:
		verbose_name_plural = "Aportes"

	def __str__(self):
		return self.foro.nombre
		
	def __documento__(self):
		lista = []
		for obj in self.adjuntos.all():
			lista.append(obj)
		return lista

	def __fotos__(self):
		lista = []
		for obj in self.fotos.all():
			lista.append(obj)
		return lista

	def __video__(self):
		lista = []
		for obj in self.video.all():
			lista.append(obj)
		return lista

	def __audio__(self):
		lista = []
		for obj in self.audio.all():
			lista.append(obj)
		return lista

class Comentarios(models.Model):
	fecha = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	comentario = RichTextUploadingField()
	aporte = models.ForeignKey(Aportes,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Comentarios"

	def __str__(self):
		return self.usuario.username
