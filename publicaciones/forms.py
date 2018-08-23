# -*- coding: utf-8 -*-
from django.db import models
from .models import *
from django import forms

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