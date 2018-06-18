# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
# from thumbs_logo import ImageWithThumbsField
from sorl.thumbnail import ImageField
from utils import *
# from south.modelsinspector import add_introspection_rules
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

# add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

# add_introspection_rules ([], ["^contrapartes\.models\.ColorField"])

# Create your models here.
from contrapartes.widgets import ColorPickerWidget

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    codigo = models.CharField(max_length=2, help_text='Código de 2 letras del país, ejemplo : Nicaragua (ni)')

    class Meta:
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Contraparte(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField("Siglas o nombre corto",help_text="Siglas o nombre corto de la oganización",max_length=200,blank=True, null=True)
    logo = ImageField(upload_to=get_file_path,null=True, blank=True)
    fileDir = 'contrapartes/logos/'
    pais = models.ForeignKey(Pais,on_delete=models.DO_NOTHING)
    fundacion = models.CharField('Año de fundación', max_length=200, 
                                 blank=True, null=True)
    temas = RichTextUploadingField(blank=True, null=True)
    generalidades = RichTextUploadingField(blank=True, null=True)
    contacto = models.CharField(max_length=200,blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    #sitio_web = models.URLField(blank=True, null=True)
    #rss = models.CharField(max_length=200,blank=True, null=True)
    font_color = ColorField(blank=True,unique=True)
    slug = models.SlugField(max_length=200,editable=False)

    class Meta:
        verbose_name_plural = "Contrapartes"
        unique_together = ("font_color", "nombre")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return '/contrapartes/%d/' % (self.id,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        return super(Contraparte, self).save(*args, **kwargs)
        
REDES_CHOICES = (('Sitio web','Sitio web'),('Facebook','Facebook'),('Twitter','Twitter'),('Youtube','Youtube'),
					('Google+','Google+'),('Instagram','Instagram'),('Linkedin','Linkedin'),
					('Flickr','Flickr'),('Pinterest','Pinterest'),('Vimeo','Vimeo'),('Otra','Otra'),)

class Redes(models.Model):
	organizacion = models.ForeignKey(Contraparte,on_delete=models.DO_NOTHING)
	opcion = models.CharField(max_length=25,choices=REDES_CHOICES)
	url = models.URLField()

	class Meta:
		verbose_name = 'Red'
		verbose_name_plural = 'Redes'

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    # Other fields here
    contraparte = models.ForeignKey(Contraparte,on_delete=models.DO_NOTHING)
    avatar = ImageField(upload_to=get_file_path,null=True, blank=True)
    fileDir = 'usuario/avatar/'

    def __str__(self):
        return u"%s - %s" % (self.user.username, self.contraparte.nombre)

    def __fecha_registro__(self):
        return u"%s" % (self.user.date_joined)

    def get_absolute_url(self):
        return '/usuario/%d/' % (self.user.id)

class Mensajero(models.Model):
    user = models.ManyToManyField(User)
    fecha = models.DateField(auto_now_add=True)
    mensaje = RichTextUploadingField()
    usuario = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return u'%s - %s ' % (self.fecha, self.mensaje)