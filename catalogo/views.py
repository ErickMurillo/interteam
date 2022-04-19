from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.
def lista_catalogo(request,template='list_catalogo.html'):
	if request.method == 'GET':
		form = FiltrosCatalogo(request.GET)
		if form.is_valid():
			tipo_producto = request.GET.getlist('tipo_producto')
			tipo_servicio = request.GET.getlist('tipo_servicio')
			localizacion = request.GET.getlist('localizacion')
			organizacion = request.GET.getlist('organizacion')

			params = {}
			if tipo_producto:
				params['tipo_producto__in'] = tipo_producto
			if tipo_servicio:
				params['tipo_servicio__in'] = tipo_servicio
			if localizacion:
				params['localizacion__in'] = localizacion
			if organizacion:
				params['user__userprofile__contraparte__in'] = organizacion
			
			object_list = Producto.objects.filter(**params,publicada = True).order_by('-id','vistas')
	else:
		form = FiltrosCatalogo()
		object_list = Producto.objects.filter(publicada = True).order_by('-id','vistas')

	# if request.method == 'POST':
	# 	form = FiltrosCatalogo(request.POST)
	# 	if form.is_valid():
	# 		tipo_producto = form.cleaned_data['tipo_producto']
	# 		tipo_servicio = form.cleaned_data['tipo_servicio']
	# 		localizacion = form.cleaned_data['localizacion']
	# 		organizacion = form.cleaned_data['organizacion']

	# 		params = {}
	# 		if tipo_producto:
	# 			   params['tipo_producto__in'] = tipo_producto
	# 		if tipo_servicio:
	# 			   params['tipo_servicio__in'] = tipo_servicio
	# 		if localizacion:
	# 			   params['localizacion__in'] = localizacion
	# 		if organizacion:
	# 			   params['user__userprofile__contraparte__in'] = organizacion

	# 		object_list = Producto.objects.filter(**params,publicada = True).order_by('-id','vistas')
	# else:
	# 	form = FiltrosCatalogo()
	# 	object_list = Producto.objects.filter(publicada = True).order_by('-id','vistas')

	return render(request, template, locals())

def detalle_catalogo(request,id,slug,template='detalle_catalogo.html'):
	object = get_object_or_404(Producto, id=id, slug=slug)
	object.vistas = object.vistas + 1
	object.save()
	productos_relacionados = Producto.objects.filter(publicada = True,tipo_producto__in = object.tipo_producto.all()).exclude(id = object.id)

	return render(request, template, locals())
