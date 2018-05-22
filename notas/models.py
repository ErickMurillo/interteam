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

# add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# Create your models here.

class Notas(models.Model):
	titulo = models.CharField(max_length=200)
	foto = ImageField(upload_to='notas/',null=True, blank=True)
	slug = models.SlugField(max_length=200,editable=False)
	fecha = models.DateField('Fecha de publicación', auto_now_add=True)
	contenido = RichTextUploadingField()
	fotos = fields.GenericRelation(Imagen)
	adjuntos = fields.GenericRelation(Documentos)
	tags = TaggableManager("Tags",help_text='Separar elementos con "," ', blank=True)

	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

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
