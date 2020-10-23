# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import *
from agendas.models import *
from contrapartes.models import *
from publicaciones.models import *
from galerias.models import *
from opiniones.models import *
from .forms import *
from biblioteca.models import *
from configuracion.models import *
# from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import thread
import datetime
import operator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.db.models import Q
from catalogo.models import *

def index(request,template='index.html'):

	notas = Notas.objects.filter(publicada = True).order_by('-fecha','-id')[:6]
	notas2 = Notas.objects.filter(publicada = True).order_by('-fecha','-id')[1:9]
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy,publico=True).order_by('-inicio','-hora_inicio')[:4]
	paises = Pais.objects.all()
	contrapartes = Contraparte.objects.all()

	publicaciones = Publicacion.objects.order_by('-id')[:3]
	catalogo = Producto.objects.order_by('-id')[:3]

	#galerias
	galerias = {}
	for x in Temas.objects.all():
		galeria = GaleriaImagenes.objects.filter(tematica = x).order_by('-id')[:2]
		if galeria.exists():
			galerias[x] = galeria

	#opiniones
	opiniones = Opiniones.objects.order_by('-id')

	#banner
	banners = BannerIndex.objects.all()

	#banner porposito
	imagenes_prop = BannerProposito.objects.order_by('id')

	return render(request, template, locals())

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def lista_notas(request,template='blog.html'):
	if request.GET.get('buscar'):
		q = request.GET['buscar']
		notas_list = Notas.objects.filter(Q(titulo__icontains = q) |
										Q(contenido__icontains = q) |
										Q(temas__nombre__icontains = q) |
										Q(user__userprofile__contraparte__siglas__icontains = q),publicada = True).order_by('-fecha','-id')

		notas_list_2 = Notas.objects.filter(Q(titulo__icontains = q),publicada = True).order_by('-fecha','-id')
	else:
		notas_list = Notas.objects.filter(publicada = True).order_by('-fecha','-id')

	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]
	paises = Pais.objects.all()

	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(publicada = True,temas = tema).count()
		if count != 0:
			dic_temas[tema] = count

	dic_eventos = {}
	for prox_event in eventos:
		delta = datetime.datetime(year=prox_event.inicio.year,month=prox_event.inicio.month,day=prox_event.inicio.day,minute=prox_event.hora_inicio.minute) - datetime.datetime.now()
		days = delta.days
		hours = delta.seconds/3600
		dic_eventos[prox_event] = days,hours

	return render(request, template, locals())

def detalle_notas(request, slug, template='blog-details.html'):
	nota = get_object_or_404(Notas, slug=slug)
	nota.vistas = nota.vistas + 1
	nota.save()
	ultimas_notas = Notas.objects.filter(publicada = True).exclude(slug = slug).order_by('-fecha','-id')[:4]
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]

	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema,publicada = True).count()
		if count != 0:
			dic_temas[tema] = count

	dic_eventos = {}
	for prox_event in eventos:
		delta = datetime.datetime(year=prox_event.inicio.year,month=prox_event.inicio.month,day=prox_event.inicio.day,minute=prox_event.hora_inicio.minute) - datetime.datetime.now()
		days = delta.days
		hours = delta.seconds/3600
		dic_eventos[prox_event] = days,hours


	if request.method == 'POST':
		form = ComentarioForm(request.POST)

		if form.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.user = request.user
			form_uncommited.nota = nota
			form_uncommited.save()

		return HttpResponseRedirect('/notas/%d/#cmt%d' % (nota.id,form.instance.id) )

	else:
		form = ComentarioForm()

	return render(request, template, locals())

def filtro_temas(request, temas, template='blog.html'):
	notas_list = Notas.objects.filter(temas__nombre = temas).order_by('-fecha','-id')
	hoy = datetime.date.today()
	eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]

	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema).count()
		if count != 0:
			dic_temas[tema] = count

	dic_eventos = {}
	for prox_event in eventos:
		delta = datetime.datetime(year=prox_event.inicio.year,month=prox_event.inicio.month,day=prox_event.inicio.day,minute=prox_event.hora_inicio.minute) - datetime.datetime.now()
		days = delta.days
		hours = delta.seconds/3600
		dic_eventos[prox_event] = days,hours

	return render(request, template, locals())

def publicaciones(request, template='publicaciones.html'):
	if request.GET.get('buscar'):
		q = request.GET['buscar']
		object_list = Publicacion.objects.filter(Q(titulo__icontains = q) |
										Q(usuario__userprofile__contraparte__siglas__icontains = q),publicada = True).order_by('-id')
	else:
		object_list = Publicacion.objects.filter(publicada = True).order_by('-id')

	count_publi = Publicacion.objects.filter(publicada = True).count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Publicacion.objects.filter(tematica = tema,publicada = True).count()
		if count != 0:
			dic_temas[tema] = count

	return render(request, template, locals())

def publicacion_detalle(request, slug, template='publicacion_detalle.html'):
	object = get_object_or_404(Publicacion, slug=slug)

	return render(request, template, locals())

def filtro_temas_publi(request, tema, template='publicaciones.html'):
	object_list = Publicacion.objects.filter(publicada = True,tematica__nombre = tema).order_by('-id')

	count_publi = Publicacion.objects.filter(publicada = True).count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Publicacion.objects.filter(publicada = True,tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count
	return render(request, template, locals())

def organizaciones(request, template='organizaciones.html'):
	object_list = Contraparte.objects.order_by('nombre')

	return render(request, template, locals())

def detalle_organizacion(request, slug, template='detalle_org.html'):
	object = get_object_or_404(Contraparte, slug=slug)

	return render(request, template, locals())

def contacto(request, template='contacto.html'):
	return render(request, template, locals())
