# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Producto
        exclude = ('user',)

class Propuesta_valorForm(forms.ModelForm):
    class Meta:
        model = Propuesta_valor
        fields = '__all__'

class FotosProductoForm(forms.ModelForm):
    class Meta:
        model = FotosProducto
        fields = '__all__'

class ArchivosProductoForm(forms.ModelForm):
    class Meta:
        model = ArchivosProducto
        fields = '__all__'
