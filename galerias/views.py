# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import *
import datetime
from notas.models import *
from agendas.models import *

# Create your views here.

def lista_galerias_img(request,template='list_galerias.html'):
	object_list = GaleriaImagenes.objects.order_by('-id')

	count_galerias = GaleriaImagenes.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaImagenes.objects.filter(tematica = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

def detalle_galerias_img(request,id, template='detalle_galeria.html'):
	object = get_object_or_404(GaleriaImagenes, id = id)
	ultimas_notas = Notas.objects.order_by('-fecha','-id')[:4]
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]

	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaImagenes.objects.filter(tematica = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

def lista_galerias_videos(request,template='list_galerias.html'):
	object_list = GaleriaVideos.objects.order_by('-id')
	count_galerias = GaleriaVideos.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaVideos.objects.filter(tematica = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

def filtro_temas_img(request,tema,template='list_galerias.html'):
	object_list = GaleriaImagenes.objects.filter(tematica = tema).order_by('-id')

	count_galerias = GaleriaImagenes.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaImagenes.objects.filter(tematica = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

def filtro_temas_vid(request,tema,template='list_galerias.html'):
	object_list = GaleriaVideos.objects.filter(tematica = tema).order_by('-id')

	count_galerias = GaleriaVideos.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = GaleriaVideos.objects.filter(tematica = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())