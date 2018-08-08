from django.shortcuts import render
from .models import *
from django.db.models import Q
from notas.models import *

# Create your views here.
def list_biblioteca(request, template='biblioteca.html'):
	if request.GET.get('buscar'):
		q = request.GET['buscar']
		object_list = Archivos.objects.filter(Q(titulo__icontains = q) | 
										Q(autor__icontains = q) |
										Q(editorial__icontains = q)|
										Q(lugar__icontains = q) |
										Q(isbn__icontains = q) |
										Q(tematica__nombre__icontains = q)|
										Q(resumen__icontains = q)).order_by('-id')
	else:
		object_list = Archivos.objects.order_by('-id')

	count_publi = Archivos.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Archivos.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count

	dic_cat = {}
	for cat in Categoria.objects.all():
		count = Archivos.objects.filter(categoria = cat).count()
		if count != 0:
			dic_cat[cat] = count

	return render(request, template, locals())

def filtro_tema_biblioteca(request, tema, template='biblioteca.html'):
	if request.GET.get('buscar'):
		q = request.GET['buscar']
		object_list = Archivos.objects.filter(Q(titulo__icontains = q) | 
										Q(autor__icontains = q) |
										Q(editorial__icontains = q)|
										Q(lugar__icontains = q) |
										Q(isbn__icontains = q) |
										Q(tematica__nombre__icontains = q)|
										Q(resumen__icontains = q)).order_by('-id')
	else:
		object_list = Archivos.objects.filter(tematica__nombre = tema)

	count_publi = Archivos.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Archivos.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count

	dic_cat = {}
	for cat in Categoria.objects.all():
		count = Archivos.objects.filter(categoria = cat).count()
		if count != 0:
			dic_cat[cat] = count

	return render(request, template, locals())

def filtro_categoria_biblioteca(request, categoria, template='biblioteca.html'):
	if request.GET.get('buscar'):
		q = request.GET['buscar']
		object_list = Archivos.objects.filter(Q(titulo__icontains = q) | 
										Q(autor__icontains = q) |
										Q(editorial__icontains = q)|
										Q(lugar__icontains = q) |
										Q(isbn__icontains = q) |
										Q(tematica__nombre__icontains = q)|
										Q(resumen__icontains = q)).order_by('-id')
	else:
		object_list = Archivos.objects.filter(categoria__nombre = categoria)

	count_publi = Archivos.objects.all().count()
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Archivos.objects.filter(tematica = tema).count()
		if count != 0:
			dic_temas[tema] = count

	dic_cat = {}
	for cat in Categoria.objects.all():
		count = Archivos.objects.filter(categoria = cat).count()
		if count != 0:
			dic_cat[cat] = count

	return render(request, template, locals())

def detail_biblioteca(request, slug, template='detalle_biblioteca.html'):
	object = Archivos.objects.get(slug=slug)

	return render(request, template, locals())