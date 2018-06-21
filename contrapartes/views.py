from django.shortcuts import render
from .models import *
from .forms import *
from notas.models import *
from notas.forms import *
from agendas.models import *
from agendas.forms import *
from foros.forms import *
from publicaciones.models import *
from publicaciones.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import get_object_or_404, redirect
from django.forms import inlineformset_factory

# Create your views here.
@login_required
def perfil_editar(request,template='admin/editar_user.html'):
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/profile/')
	else:
		form = UserForm(instance=request.user)

	return render(request, template, locals())

@login_required
def editar_contraparte(request, slug, template='admin/editar_contraparte.html'):
	contra = get_object_or_404(Contraparte, slug=slug)
	FormSetInit = inlineformset_factory(Contraparte, Redes, form=RedesFrom,extra=11,max_num=11)

	if request.method == 'POST':
		form = ContraparteForms(data=request.POST,instance=contra,files=request.FILES)
		formset = FormSetInit(request.POST,request.FILES,instance=contra)

		if form.is_valid() and formset.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.user = request.user
			form_uncommited.save()

			formset.save()
			return HttpResponseRedirect('/accounts/profile/')
	else:
		form = ContraparteForms(instance=contra)
		formset = FormSetInit(instance=contra)

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
def redactar_notas_contraparte(request, template='admin/redactar_notaadmin.html'):
	if request.method == 'POST':
		form = NotasForms(request.POST, request.FILES)
		if form.is_valid():
			nota = form.save(commit=False)
			nota.user = request.user
			nota.save()
			form.save_m2m()

			return HttpResponseRedirect('/contrapartes/notas/')
	else:
		form = NotasForms()

	return render(request, template, locals())

@login_required
def filtro_temas_contra(request, temas, template='admin/notaadmin.html'):
	object_list = Notas.objects.filter(user_id = request.user.id,temas__nombre = temas).order_by('-id')
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

@login_required
def eventos_contraparte(request, template='admin/list_eventos.html'):
	object_list = Agendas.objects.filter(user_id = request.user.id)

	return render(request, template, locals())

@login_required
def nuevo_evento_contraparte(request, template='admin/nuevo_evento.html'):
	if request.method == 'POST':
		form = AgendaForm(request.POST, request.FILES)
		if form.is_valid():
			nota = form.save(commit=False)
			nota.user = request.user
			nota.save()

			return HttpResponseRedirect('/contrapartes/eventos/')
	else:
		form = AgendaForm()

	return render(request, template, locals())

@login_required
def eliminar_evento_contraparte(request, slug):
	evento = Agendas.objects.filter(slug = slug).delete()
	return HttpResponseRedirect('/contrapartes/eventos/')

@login_required
def editar_evento(request, slug, template='admin/editar_evento.html'):
	object = get_object_or_404(Agendas, slug=slug)
	if request.method == 'POST':
		form = AgendaForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.user = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/contrapartes/eventos/')
	else:
		form = AgendaForm(instance=object)

	return render(request, template, locals())

#foros
@login_required
def list_foros(request, template='admin/list_foros.html'):
	object_list = Foros.objects.order_by('-id')
	mis_foros = Foros.objects.filter(contraparte = request.user.id).order_by('-id')

	return render(request, template, locals())

@login_required
def eliminar_foro(request, id):
	foro = Foros.objects.filter(id = id).delete()
	return HttpResponseRedirect('/contrapartes/foros/')

@login_required
def editar_foro(request, id, template='admin/editar_foro.html'):
	object = get_object_or_404(Foros, id=id)
	if request.method == 'POST':
		form = ForosForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.contraparte = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/contrapartes/foros/')
	else:
		form = ForosForm(instance=object)

	return render(request, template, locals())

@login_required
def ver_foro(request, id, template='admin/ver_foro.html'):
	discusion = get_object_or_404(Foros, id=id)  
	aportes = Aportes.objects.filter(foro = id).order_by('-id')
	if request.method == 'POST':
		form = AporteForm(request.POST)
		if form.is_valid():
			aporte = form.save(commit=False)
			aporte.foro = discusion
			aporte.user = request.user
			aporte.save()
			return redirect('ver-foro', id=discusion.id)
	else:
		form = AporteForm()
	return render(request, template, locals())

@login_required
def agregar_foro(request, template='admin/nuevo_foro.html'):
	if request.method == 'POST':
		form = ForosForm(request.POST, request.FILES)
		if form.is_valid():
			foro = form.save(commit=False)
			foro.contraparte = request.user
			foro.save()

			return HttpResponseRedirect('/contrapartes/foros/')
	else:
		form = ForosForm()

	return render(request, template, locals())

#publicaciones
@login_required
def publicaciones_contraparte(request, template='admin/list_publicaciones.html'):
	object_list = Publicacion.objects.filter(usuario = request.user.id).order_by('-id')

	return render(request, template, locals())

@login_required
def eliminar_publicacion(request, id):
	evento = Publicacion.objects.filter(id = id).delete()
	return HttpResponseRedirect('/contrapartes/publicaciones/')

@login_required
def editar_publicacion(request, id, template='admin/editar_publicacion.html'):
	object = get_object_or_404(Publicacion, id=id)
	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.usuario = request.user
			form_uncommited.save()
			return HttpResponseRedirect('/contrapartes/publicaciones/')
	else:
		form = PublicacionForm(instance=object)

	return render(request, template, locals())

@login_required
def agregar_publicacion(request, template='admin/nueva_publicacion.html'):
	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES)
		if form.is_valid():
			publi = form.save(commit=False)
			publi.usuario = request.user
			publi.save()

			return HttpResponseRedirect('/contrapartes/publicaciones/')
	else:
		form = PublicacionForm()

	return render(request, template, locals())

@login_required
def editar_aporte(request, id, template='admin/editar_aporte.html'):
	object = get_object_or_404(Aportes, id=id)
	if request.method == 'POST':
		form = AporteForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.user = request.user
			form_uncommited.save()
			return redirect('ver-foro', id=object.foro.id)
	else:
		form = AporteForm(instance=object)

	return render(request, template, locals())

@login_required
def eliminar_aporte(request, id):
	aporte = Aportes.objects.get(id = id)
	foro = aporte.foro.id
	aporte.delete()
	return redirect('ver-foro', id=foro)