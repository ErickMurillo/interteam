# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.contenttypes import fields
from contrapartes.models import *
from foros.models import *
from django.template.defaultfilters import slugify
# from south.modelsinspector import add_introspection_rules
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from taggit_autosuggest.managers import TaggableManager
from embed_video.fields import EmbedVideoField

# add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# Create your models here.
class Temas(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta: 
		verbose_name_plural = 'Temas'
		verbose_name = 'Tema'

	def __str__(self):
		return self.nombre

TIPO_CHOICES = ((1,'Foto'),(2,'Video'))

class Notas(models.Model):
	titulo = models.CharField(max_length=200)
	tipo = models.IntegerField(choices=TIPO_CHOICES)
	foto = ImageField(upload_to='notas/',null=True, blank=True)
	video = EmbedVideoField('Video (url)',null=True, blank=True)
	slug = models.SlugField(max_length=200,editable=False)
	fecha = models.DateField('Fecha de publicación', auto_now_add=True)
	contenido = RichTextUploadingField()
	#fotos = fields.GenericRelation(Imagen)
	#adjuntos = fields.GenericRelation(Documentos)
	temas = models.ManyToManyField(Temas)
	tags = TaggableManager("Tags",help_text='Separar elementos con "," ', blank=True)
	vistas = models.IntegerField(editable=False,default=0)

	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	publicada = models.BooleanField()
	correo_enviado = models.BooleanField(editable=False)

	class Meta:
		verbose_name_plural = "Notas"
		ordering = ['-fecha','-id']

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(Notas, self).save(*args, **kwargs)

	def imagenes(self):
		imagenes = Imagen.objects.filter(object_id=self.id)
		return imagenes

	def adjunto(self):
		adjunto = Documentos.objects.filter(object_id=self.id)
		return adjunto

	def get_absolute_url(self):
		return '/notas/%d/' % (self.id,)
	# Para obtener el pais de la noticia
	def pais(self):
		usuario = UserProfile.objects.get(pk=self.user.id)
		contraparte = Contraparte.objects.get(pk=usuario.contraparte.id)
		pais = Pais.objects.get(pk=contraparte.pais.id)
		return pais

	# Para obtener la contraparte de la noticia
	def contraparte(self):
		usuario = UserProfile.objects.get(pk=self.user.id)
		contraparte = Contraparte.objects.get(pk=usuario.contraparte.id)
		return contraparte

class ComentarioNotas(models.Model):
	nota = models.ForeignKey(Notas,on_delete=models.DO_NOTHING)
	fecha = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	comentario = RichTextUploadingField()

	def __str__(self):
		return self.user.username
