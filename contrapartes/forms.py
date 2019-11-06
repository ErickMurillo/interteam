# -*- coding: UTF-8 -*-
from django.db import models
from django.forms import ModelForm
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import User
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, SelectDateWidget
from contrapartes.widgets import ColorPickerWidget

class ContraparteForms(forms.ModelForm):
	temas = forms.CharField(widget=CKEditorUploadingWidget())
	siglas = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Siglas o nombre corto"}))
	generalidades = forms.CharField(widget=CKEditorUploadingWidget())
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Nombre completo de la contraparte"}))
	fundacion = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Año en que fue fundada la organización"}))
	contacto = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Nombre completo de la persona de contacto"}))
	correo = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Correo de la persona de contacto"}))
	telefono = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Formato ### - ######## "}))
	#sitio_web = forms.URLField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Con este formato http://www.dominio.com "}))
	# rss = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Dirección rss de contenido sindicado"}))
	#font_color = forms.CharField(required=False, widget=ColorPickerWidget, label="Color")

	class Meta:
		model = Contraparte
		exclude = ('user',)

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar',)

from django.forms import ModelMultipleChoiceField

class UserModelMultipleChoiceField(ModelMultipleChoiceField):
	def label_from_instance(self, obj):
		try:
			user_profile = UserProfile.objects.get(user = obj)
			return "%s - %s" % (obj.username,user_profile.contraparte.siglas)
		except:
			pass	

class MensajeForm(forms.ModelForm):
	user = UserModelMultipleChoiceField(queryset = User.objects.order_by('username'))
	mensaje = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		#widgets = {'user': forms.CheckboxSelectMultiple}
		model = Mensajero
		exclude = ('usuario','fecha')

class RedesFrom(forms.ModelForm):
	class Meta:
		model = Redes
		fields = '__all__'
		exclude = ['organizacion',]
