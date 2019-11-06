# -*- coding: UTF-8 -*-

from django.db import models
# from foros.models import Documentos
from django.contrib.contenttypes import fields
from django.contrib.auth.models import User
# from south.modelsinspector import add_introspection_rules
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from utils import *

# add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# Create your models here.

class Agendas(models.Model):
    evento = models.CharField(max_length=200)
    foto = ImageField(upload_to='eventos/',null=True, blank=True)
    descripcion = RichTextUploadingField()
    inicio = models.DateField('Fecha de Inicio')
    final = models.DateField('Fecha de Finalización',null=True, blank=True)
    hora_inicio = models.TimeField('Hora inicio')
    hora_fin = models.TimeField('Hora fin')
    lugar = models.CharField(max_length=250)
    publico = models.BooleanField()
    # adjunto = fields.GenericRelation(Documentos)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200,editable=False)
    correo_enviado = models.BooleanField(editable=False)

    class Meta:
    	verbose_name_plural = "Agendas"

    def __str__(self):
    	return u'%s' % self.evento

    def get_absolute_url(self):
        return '/agendas/%d/' % (self.id,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.evento)
        return super(Agendas, self).save(*args, **kwargs)

class AgendaEvento(models.Model):
    evento = models.ForeignKey(Agendas,on_delete=models.CASCADE)
    actividad = models.CharField(max_length=200)
    fecha = models.DateField()
    hora_inicio = models.TimeField('Hora inicio')
    hora_fin = models.TimeField('Hora fin')
    descripcion = models.CharField(max_length=600)

class DocumentosEvento(models.Model):
    evento = models.ForeignKey(Agendas,on_delete=models.CASCADE)
    nombre_doc = models.CharField("Nombre",max_length=200)
    adjunto = models.FileField("Adjunto",upload_to=get_file_path)

    fileDir = 'documentos/'

    class Meta:
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.nombre_doc