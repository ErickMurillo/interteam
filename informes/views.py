from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import collections
from django.db.models.functions import ExtractYear 

# Create your views here.
@login_required
def detalle_informe(request,slug,template='informes/detalle.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	rango = RangoFechaImagenes.objects.filter(proyecto = object.id)
	dict = collections.OrderedDict()
	for fecha in rango:
		imagenes = Imagenes.objects.filter(rango = fecha.id)
		dict[fecha.inicio,fecha.fin] = imagenes

	return render(request, template, locals())

@login_required
def lista_informes(request,slug,template='informes/informes.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	object_list = Informe.objects.filter(proyecto__slug = slug)
	anios = object_list.annotate(year=ExtractYear('fecha_informe')).distinct('year').values_list('year', flat=True)
	return render(request, template, locals())

def lista_documentos(request,slug,template='informes/documentos.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	object_list = Documento.objects.filter(proyecto__slug = slug)
	return render(request, template, locals())

def imagenes(request,slug,template='informes/imagenes.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	rango = RangoFechaImagenes.objects.filter(proyecto = object.id)
	dict = collections.OrderedDict()
	for fecha in rango:
		imagenes = Imagenes.objects.filter(rango = fecha.id)
		dict[fecha.inicio,fecha.fin] = imagenes

	return render(request, template, locals())

def videos(request,slug,template='informes/videos.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	object_list = Video.objects.filter(proyecto__slug = slug)
	return render(request, template, locals())

def anexos(request,slug,template='informes/anexos.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	object_list = Monitoreo.objects.filter(proyecto__slug = slug)
	return render(request, template, locals())



