# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from contrapartes.models import *
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

class FiltrosCatalogo(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FiltrosCatalogo, self).__init__(*args, **kwargs)
        self.fields['tipo_producto'] = forms.ModelMultipleChoiceField(queryset=TipoProducto.objects.order_by('nombre'), required=False)
        self.fields['tipo_servicio'] = forms.ModelMultipleChoiceField(queryset=ServiciosProducto.objects.order_by('nombre'), required=False)
        self.fields['localizacion'] = forms.ModelMultipleChoiceField(queryset=Departamento.objects.order_by('nombre'), required=False)
        self.fields['organizacion'] = forms.ModelMultipleChoiceField(queryset=Contraparte.objects.order_by('nombre'), required=False)
