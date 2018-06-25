# -*- coding: utf-8 -*-
from django.db import models
from .models import *
from django import forms

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		exclude = ('usuario',)