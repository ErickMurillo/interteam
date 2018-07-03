from django.shortcuts import render
from .models import *
from django.db.models import Q

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

	return render(request, template, locals())

def detail_biblioteca(request, slug, template='detalle_biblioteca.html'):
	object = Archivos.objects.get(slug=slug)

	return render(request, template, locals())