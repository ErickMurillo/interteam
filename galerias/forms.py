# -*- coding: utf-8 -*-
from django.db import models
from .models import *
from django import forms

class GaleriaImagenesForm(forms.ModelForm):
	class Meta:
		model = GaleriaImagenes
		exclude = ('user',)

class ImagenesForm(forms.ModelForm):
	class Meta:
		model = Imagenes
		fields = '__all__'

class GaleriaVideosForm(forms.ModelForm):
	class Meta:
		model = GaleriaVideos
		exclude = ('user',)