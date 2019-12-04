from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def detalle_informe(request,slug,template='informes/detalle.html'):
	object = get_object_or_404(Proyecto, slug=slug)
	return render(request, template, locals())

@login_required
def lista_informes(request,slug,template='informes/informes.html'):
	object_list = Informe.objects.filter(proyecto__slug = slug)
	return render(request, template, locals())

def lista_documentos(request,slug,template='informes/documentos.html'):
	object_list = Documento.objects.filter(proyecto__slug = slug)
	return render(request, template, locals())

def imagenes(request,slug,template='informes/imagenes.html'):
	object_list = Imagenes.objects.filter(rango__proyecto__slug = slug)
	return render(request, template, locals())

def videos(request,slug,template='informes/videos.html'):
	object_list = Video.objects.filter(proyecto__slug = slug)
	return render(request, template, locals())



