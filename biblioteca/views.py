from django.shortcuts import render
from .models import *

# Create your views here.
def list_biblioteca(request, template='biblioteca.html'):
	object_list = Archivos.objects.order_by('-id')

	return render(request, template, locals())

def detail_biblioteca(request, slug, template='detalle_biblioteca.html'):
	object = Archivos.objects.get(slug=slug)

	return render(request, template, locals())