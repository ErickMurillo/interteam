from django.shortcuts import render
from .models import *
from .forms import *
from notas.models import *
from notas.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def editar_contraparte(request, slug, template='admin/editar_contraparte.html'):
	contra = get_object_or_404(Contraparte, slug=slug)

	if request.method == 'POST':
		form = ContraparteForms(data=request.POST, 
								instance=contra, 
								files=request.FILES)
		if form.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.user = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/accounts/profile/')
	else:
		form = ContraparteForms(instance=contra)

	return render(request, template, locals())

@login_required
def notas_contraparte(request, template='admin/notaadmin.html'):
	object_list = Notas.objects.filter(user_id = request.user.id)
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

@login_required
def filtro_temas_contra(request, temas, template='admin/notaadmin.html'):
	object_list = Notas.objects.filter(user_id = request.user.id,temas__nombre = temas)
	dic_temas = {}
	for tema in Temas.objects.all():
		count = Notas.objects.filter(temas = tema).count()
		dic_temas[tema] = count

	return render(request, template, locals())

@login_required
def editar_nota(request, slug, template='admin/editar_nota.html'):
	object = get_object_or_404(Notas, slug=slug)
	if request.method == 'POST':
		form = NotasForms(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.user = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/contrapartes/notas/')
	else:
		form = NotasForms(instance=object)

	return render(request, template, locals())

@login_required
def eliminar_notas_contraparte(request, slug):
	nota = Notas.objects.filter(slug = slug).delete()
	return HttpResponseRedirect('/contrapartes/notas/')

