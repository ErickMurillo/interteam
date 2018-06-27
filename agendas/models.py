# -*- coding: UTF-8 -*-

from django.db import models
from foros.models import Documentos
from django.contrib.contenttypes import fields
from django.contrib.auth.models import User
# from south.modelsinspector import add_introspection_rules
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify

# add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# Create your models here.

class Agendas(models.Model):
    evento = models.CharField(max_length=200)
    foto = ImageField(upload_to='eventos/',null=True, blank=True)
    descripcion = RichTextUploadingField()
    inicio = models.DateField('Fecha de Inicio')
    # final = models.DateField('Fecha de Finalización')
    hora_inicio = models.TimeField('Hora inicio')
    hora_fin = models.TimeField('Hora fin')
    lugar = models.CharField(max_length=250)
    publico = models.BooleanField()
    adjunto = fields.GenericRelation(Documentos)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200,editable=False)

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
    evento = models.ForeignKey(Agendas,on_delete=models.DO_NOTHING)
    actividad = models.CharField(max_length=200)
    hora_inicio = models.TimeField('Hora inicio')
    hora_fin = models.TimeField('Hora fin')
    descripcion = models.CharField(max_length=600)