# -*- coding: utf-8 -*-
from django.db import models
from .models import *
from django import forms
from contrapartes.models import *

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		exclude = ('usuario',)

class ArchivosPubliForm(forms.ModelForm):
	class Meta:
		model = ArchivosPublicacion
		fields = '__all__'

class AudiosPubliForm(forms.ModelForm):
	class Meta:
		model = AudiosPublicacion
		fields = '__all__'

class VideosPubliForm(forms.ModelForm):
	class Meta:
		model = VideosPublicacion
		fields = '__all__'

def organizaciones():
	lista = []
	foo = Publicacion.objects.order_by('usuario__userprofile__contraparte').distinct('usuario__userprofile__contraparte').values_list('usuario__userprofile__contraparte__id', flat=True)
	for x in Contraparte.objects.filter(id__in=foo):
		lista.append((x.id,x.siglas))
	return lista

class FiltrosBiblioteca(forms.Form):
	def __init__(self, *args, **kwargs):
		super(FiltrosBiblioteca, self).__init__(*args, **kwargs)
		self.fields['informacion'] = forms.ModelMultipleChoiceField(queryset=Informacion.objects.order_by('nombre'), required=False)
		self.fields['herramientas'] = forms.ModelMultipleChoiceField(queryset=Herramientas.objects.order_by('nombre'), required=False)
		self.fields['organizaciones'] = forms.MultipleChoiceField(choices=organizaciones(), required=False)
