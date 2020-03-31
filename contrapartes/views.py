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
from galerias.models import *
from galerias.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import get_object_or_404, redirect
from django.forms import inlineformset_factory
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
@login_required
def perfil_editar(request,template='admin/editar_user.html'):
	object = get_object_or_404(UserProfile, user=request.user)
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		form_avatar = UserProfileForm(request.POST,files=request.FILES,instance=object)
		if form.is_valid() and form_avatar.is_valid():
			form.save()
			form_avatar.save()
			return HttpResponseRedirect('/accounts/profile/')
	else:
		form = UserForm(instance=request.user)
		form_avatar = UserProfileForm(instance=object)

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
		count = Notas.objects.filter(temas = tema,user = request.user).count()
		if count != 0:
			dic_temas[tema] = count

	return render(request, template, locals())

@login_required
def redactar_notas_contraparte(request, template='admin/redactar_notaadmin.html'):
	if request.method == 'POST':
		form = NotasForms(request.POST, request.FILES)
		if form.is_valid():
			nota = form.save(commit=False)
			nota.user = request.user
			nota.correo_enviado = False
			nota.save()
			form.save_m2m()

			if nota.publicada == True:
				try:
					subject, from_email = 'Nueva nota', 'cluster.nicaragua@gmail.com'
					text_content =  render_to_string('email/nota.txt', {'nota': nota,})

					html_content = render_to_string('email/nota.txt', {'nota': nota,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					enviado = 1
					nota.correo_enviado = True
					nota.save()
					return HttpResponseRedirect('/contrapartes/notas/')
				except:
					pass
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

			if form_uncommited.publicada == True and form_uncommited.correo_enviado == False:
				try:
					subject, from_email = 'Nueva nota', 'cluster.nicaragua@gmail.com'
					text_content =  render_to_string('email/nota.txt', {'nota': form_uncommited,})

					html_content = render_to_string('email/nota.txt', {'nota': form_uncommited,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					form_uncommited.correo_enviado = True
					form_uncommited.save()
					return HttpResponseRedirect('/contrapartes/notas/')
				except:
					pass

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
	FormSetInit = inlineformset_factory(Agendas,AgendaEvento,form=AgendaEventoForm,extra=12,max_num=12)
	FormSetInit2 = inlineformset_factory(Agendas,DocumentosEvento,form=DocuForm,extra=6,max_num=6)

	if request.method == 'POST':
		form = AgendaForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		formset2 = FormSetInit2(request.POST,request.FILES)
		if form.is_valid() and formset.is_valid() and formset2.is_valid():
			evento = form.save(commit=False)
			evento.user = request.user
			evento.correo_enviado = False
			evento.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.evento = evento
				instance.save()
			formset.save_m2m()
			
			instances2 = formset2.save(commit=False)
			for instance2 in instances2:
				instance2.evento = evento
				instance2.save()
			formset2.save_m2m()

			if evento.publico == True:
				try:
					subject, from_email = 'Nuevo evento', 'cluster.nicaragua@gmail.com'
					text_content = render_to_string('email/evento.txt', {'evento': evento,})

					html_content = render_to_string('email/evento.txt', {'evento': evento,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					evento.correo_enviado = True
					evento.save()
					return HttpResponseRedirect('/contrapartes/eventos/')
				except:
					pass

	else:
		form = AgendaForm()
		formset = FormSetInit()
		formset2 = FormSetInit2()

	return render(request, template, locals())

@login_required
def eliminar_evento_contraparte(request, slug):
	evento = Agendas.objects.get(slug = slug).delete()
	return HttpResponseRedirect('/contrapartes/eventos/')

@login_required
def editar_evento(request, slug, template='admin/editar_evento.html'):
	object = get_object_or_404(Agendas, slug=slug)
	FormSetInit = inlineformset_factory(Agendas,AgendaEvento,form=AgendaEventoForm,extra=12,max_num=12)
	FormSetInit2 = inlineformset_factory(Agendas,DocumentosEvento,form=DocuForm,extra=6,max_num=6)

	if request.method == 'POST':
		form = AgendaForm(request.POST, request.FILES,instance=object)
		formset = FormSetInit(request.POST,request.FILES,instance=object)
		formset2 = FormSetInit2(request.POST,request.FILES,instance=object)

		if form.is_valid() and formset.is_valid() and formset2.is_valid():
			evento = form.save(commit=False)
			evento.user = request.user
			evento.correo_enviado = False
			evento.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.evento = evento
				instance.save()
			formset.save_m2m()
			
			instances2 = formset2.save(commit=False)
			for instance2 in instances2:
				instance2.evento = evento
				instance2.save()
			formset2.save_m2m()

			if evento.publico == True and evento.correo_enviado == False:
				try:
					subject, from_email = 'Nuevo evento', 'cluster.nicaragua@gmail.com'
					text_content = render_to_string('email/evento.txt', {'evento': evento,})

					html_content = render_to_string('email/evento.txt', {'evento': evento,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					evento.correo_enviado = True
					evento.save()
					return HttpResponseRedirect('/contrapartes/eventos/')
				except:
					pass

			return HttpResponseRedirect('/contrapartes/eventos/')
	else:
		form = AgendaForm(instance=object)
		formset = FormSetInit(instance=object)
		formset2 = FormSetInit2(instance=object)

	return render(request, template, locals())

#foros
@login_required
def list_foros(request, template='admin/list_foros.html'):
	current_date = datetime.date.today()
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
	current_date = datetime.date.today()
	discusion = get_object_or_404(Foros, id=id)  
	aportes = Aportes.objects.filter(foro = id).order_by('-id')
	if request.method == 'POST':
		form = AporteForm(request.POST)
		if form.is_valid():
			aporte = form.save(commit=False)
			aporte.foro = discusion
			aporte.user = request.user
			aporte.save()

			try:
				subject, from_email = 'Nuevo aporte al foro ' + discusion.nombre, 'cluster.nicaragua@gmail.com'
				text_content = render_to_string('email/aporte.txt', {'aporte': aporte,})

				html_content = render_to_string('email/aporte.txt', {'aporte': aporte,})

				list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				return redirect('ver-foro', id=discusion.id)
			except:
				pass

	else:
		form = AporteForm()

	return render(request, template, locals())

from interteam.tasks import *
import datetime
@login_required
def agregar_foro(request, template='admin/nuevo_foro.html'):
	if request.method == 'POST':
		form = ForosForm(request.POST, request.FILES)
		if form.is_valid():
			foro = form.save(commit=False)
			foro.contraparte = request.user
			foro.correo_enviado = False
			foro.save()

			hoy = datetime.date.today()
			if foro.apertura == hoy and foro.correo_enviado == False:
				try:
					subject, from_email = 'Nuevo foro', 'cluster.nicaragua@gmail.com'
					text_content = render_to_string('email/foro.txt', {'foro': foro,})

					html_content = render_to_string('email/foro.txt', {'foro': foro,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					foro.correo_enviado = True
					foro.save()
					return HttpResponseRedirect('/contrapartes/foros/')
				except:
					pass

			else:
				id = foro.id
				user = request.user.id
				send_mail_foro.apply_async((id,user),eta=foro.apertura)
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
	FormSetInit = inlineformset_factory(Publicacion,ArchivosPublicacion,form=ArchivosPubliForm,extra=9,max_num=9)
	FormSetInit2 = inlineformset_factory(Publicacion,AudiosPublicacion,form=AudiosPubliForm,extra=6,max_num=6)
	FormSetInit3 = inlineformset_factory(Publicacion,VideosPublicacion,form=VideosPubliForm,extra=6,max_num=6)

	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES, instance=object)
		formset = FormSetInit(request.POST,request.FILES, instance=object)
		formset2 = FormSetInit2(request.POST,request.FILES, instance=object)
		formset3 = FormSetInit3(request.POST,request.FILES, instance=object)

		if form.is_valid() and formset.is_valid() and formset2.is_valid() and formset3.is_valid():
			form_uncommited = form.save()
			form_uncommited.usuario = request.user
			form_uncommited.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.publicacion = form_uncommited
				instance.save()
			formset.save_m2m()
			
			instances2 = formset2.save(commit=False)
			for instance2 in instances2:
				instance2.publicacion = form_uncommited
				instance2.save()
			formset2.save_m2m()

			instances3 = formset3.save(commit=False)
			for instance3 in instances3:
				instance3.publicacion = form_uncommited
				instance3.save()
			formset3.save_m2m()

			if form_uncommited.publicada == True and form_uncommited.correo_enviado == False:
				try:
					subject, from_email = 'Nueva publicación', 'cluster.nicaragua@gmail.com'
					text_content = render_to_string('email/publicacion.txt', {'publi': form_uncommited,})

					html_content = render_to_string('email/publicacion.txt', {'publi': form_uncommited,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					form_uncommited.correo_enviado = True
					form_uncommited.save()
					return HttpResponseRedirect('/contrapartes/publicaciones/')
				except:
					pass

			return HttpResponseRedirect('/contrapartes/publicaciones/')
	else:
		form = PublicacionForm(instance=object)
		formset = FormSetInit(instance=object)
		formset2 = FormSetInit2(instance=object)
		formset3 = FormSetInit3(instance=object)

	return render(request, template, locals())

@login_required
def agregar_publicacion(request, template='admin/nueva_publicacion.html'):
	FormSetInit = inlineformset_factory(Publicacion,ArchivosPublicacion,form=ArchivosPubliForm,extra=9,max_num=9)
	FormSetInit2 = inlineformset_factory(Publicacion,AudiosPublicacion,form=AudiosPubliForm,extra=6,max_num=6)
	FormSetInit3 = inlineformset_factory(Publicacion,VideosPublicacion,form=VideosPubliForm,extra=6,max_num=6)

	if request.method == 'POST':
		form = PublicacionForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		formset2 = FormSetInit2(request.POST,request.FILES)
		formset3 = FormSetInit3(request.POST,request.FILES)

		if form.is_valid() and formset.is_valid() and formset2.is_valid() and formset3.is_valid():
			publi = form.save(commit=False)
			publi.usuario = request.user
			publi.correo_enviado = False
			publi.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.publicacion = publi
				instance.save()
			formset.save_m2m()
			
			instances2 = formset2.save(commit=False)
			for instance2 in instances2:
				instance2.publicacion = publi
				instance2.save()
			formset2.save_m2m()

			instances3 = formset3.save(commit=False)
			for instance3 in instances3:
				instance3.publicacion = publi
				instance3.save()
			formset3.save_m2m()

			if publi.publicada == True and publi.correo_enviado == False:
				try:
					subject, from_email = 'Nueva publicación', 'cluster.nicaragua@gmail.com'
					text_content = render_to_string('email/publicacion.txt', {'publi': publi,})

					html_content = render_to_string('email/publicacion.txt', {'publi': publi,})

					list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
					msg.attach_alternative(html_content, "text/html")
					msg.send()

					publi.correo_enviado = True
					publi.save()
					return HttpResponseRedirect('/contrapartes/publicaciones/')
				except:
					pass
			
	else:
		form = PublicacionForm()
		formset = FormSetInit()
		formset2 = FormSetInit2()
		formset3 = FormSetInit3()

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

@login_required
def agregar_comentario(request, id, template='admin/comentario.html'):
	object = get_object_or_404(Aportes, id=id)
	if request.method == 'POST':
		form = ComentarioForm(request.POST, request.FILES)
		if form.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.aporte = object
			form_uncommited.usuario = request.user
			form_uncommited.save()

			try:
				subject, from_email = 'Nuevo comentario al foro ' + object.foro.nombre, 'cluster.nicaragua@gmail.com'
				text_content = render_to_string('email/comentario.txt', {'object': form_uncommited,})
								
				html_content = render_to_string('email/comentario.txt', {'object': form_uncommited,})
								
				list_mail = UserProfile.objects.exclude(user__id = request.user.id).values_list('user__email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				enviado = 1

				return redirect('ver-foro', id=object.foro.id)
			except:
				pass

	else:
		form = ComentarioForm()

	return render(request, template, locals())

@login_required
def editar_comentario(request, id, template='admin/comentario.html'):
	object = get_object_or_404(Comentarios, id=id)
	if request.method == 'POST':
		form = ComentarioForm(request.POST, request.FILES,instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.aporte = object.aporte
			form_uncommited.usuario = request.user
			form_uncommited.save()

			return redirect('ver-foro', id=object.aporte.foro.id)
	else:
		form = ComentarioForm(instance=object)

	return render(request, template, locals())

@login_required
def eliminar_comentario(request, id):
	comentario = Comentarios.objects.get(id = id)
	foro = comentario.aporte.foro.id
	comentario.delete()
	return redirect('ver-foro', id=foro)
#galerias
@login_required
def galerias_contraparte(request, template='admin/list_galerias.html'):
	object_list_img = GaleriaImagenes.objects.filter(user = request.user.id).order_by('-id')
	object_list_vid = GaleriaVideos.objects.filter(user = request.user.id).order_by('-id')

	return render(request, template, locals())

@login_required
def eliminar_galeria_img(request, id):
	img = GaleriaImagenes.objects.filter(id = id).delete()
	return HttpResponseRedirect('/contrapartes/galerias/')

@login_required
def agregar_galeria_img(request, template='admin/galeria_img.html'):
	FormSetInit = inlineformset_factory(GaleriaImagenes, Imagenes, form=ImagenesForm,extra=12,max_num=12)
	if request.method == 'POST':
		form = GaleriaImagenesForm(request.POST, request.FILES)
		formset = FormSetInit(request.POST,request.FILES)
		if form.is_valid() and formset.is_valid():
			galeria = form.save(commit=False)
			galeria.user = request.user
			galeria.save()

			instances = formset.save(commit=False)
			for instance in instances:
				instance.imagenes = galeria
				instance.save()
			formset.save_m2m()

			return HttpResponseRedirect('/contrapartes/galerias/')
	else:
		form = GaleriaImagenesForm()
		formset = FormSetInit()

	return render(request, template, locals())

@login_required
def editar_galeria_img(request, id, template='admin/galeria_img.html'):
	object = get_object_or_404(GaleriaImagenes, id=id)
	FormSetInit = inlineformset_factory(GaleriaImagenes, Imagenes, form=ImagenesForm,extra=12,max_num=12)
	if request.method == 'POST':
		form = GaleriaImagenesForm(data=request.POST,instance=object,files=request.FILES)
		formset = FormSetInit(request.POST,request.FILES,instance=object)

		if form.is_valid() and formset.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.save()

			formset.save()
			return HttpResponseRedirect('/contrapartes/galerias/')
	else:
		form = GaleriaImagenesForm(instance=object)
		formset = FormSetInit(instance=object)

	return render(request, template, locals())

@login_required
def agregar_galeria_vid(request, template='admin/nueva_galeria_vid.html'):
	if request.method == 'POST':
		form = GaleriaVideosForm(request.POST, request.FILES)
		if form.is_valid():
			publi = form.save(commit=False)
			publi.user = request.user
			publi.save()

			return HttpResponseRedirect('/contrapartes/galerias/')
	else:
		form = GaleriaVideosForm()

	return render(request, template, locals())

@login_required
def eliminar_video(request, id):
	img = GaleriaVideos.objects.filter(id = id).delete()
	return HttpResponseRedirect('/contrapartes/galerias/')

@login_required
def editar_video(request, id, template='admin/nueva_galeria_vid.html'):
	object = get_object_or_404(GaleriaVideos, id=id)
	if request.method == 'POST':
		form = GaleriaVideosForm(request.POST, request.FILES, instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.user = request.user
			form_uncommited.save()
			
			return HttpResponseRedirect('/contrapartes/galerias/')
	else:
		form = GaleriaVideosForm(instance=object)

	return render(request, template, locals())

@login_required
def mensajes(request, template='admin/mensajes.html'):
	if request.method == 'POST':
		form = MensajeForm(request.POST, request.FILES)
		form.fields['user'].queryset = User.objects.exclude(id=request.user.id)

		if form.is_valid():
			form_uncommited = form.save(commit=False)
			form_uncommited.usuario = request.user
			form_uncommited.save()
			form.save_m2m()

			try:
				subject, from_email = 'Nuevo mensaje ','cluster.nicaragua@gmail.com'
				text_content = render_to_string('email/mensaje.txt', {'object': form_uncommited,})

				html_content = render_to_string('email/mensaje.txt', {'object': form_uncommited,})

				list_mail = []
				for user in form_uncommited.user.all():
					list_mail.append(user.email)

				msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				enviado = 1

			except:
				pass
			
	else:
		form  = MensajeForm()
		form.fields['user'].queryset = User.objects.exclude(id=request.user.id)
		enviado = 0

	return render(request, template, locals())

@login_required
def estadisticas(request, template='admin/estadisticas.html'):
	dic_notas = {}
	dic_foros = {}
	dic_aportes = {}
	dic_coment = {}
	list_resumen = []
	for org in Contraparte.objects.all():
		conteo = Notas.objects.filter(user__userprofile__contraparte = org).count()
		dic_notas[org.siglas] = conteo

		conteo_foros = Foros.objects.filter(contraparte__userprofile__contraparte = org).count()
		dic_foros[org.siglas] = conteo_foros

		conteo_aportes = Aportes.objects.filter(user__userprofile__contraparte = org).count()
		dic_aportes[org.siglas] = conteo_aportes

		conteo_coment = Comentarios.objects.filter(usuario__userprofile__contraparte = org).count()
		dic_coment[org.siglas] = conteo_coment

		conteo_eventos = Agendas.objects.filter(user__userprofile__contraparte = org).count()
		conteo_img = GaleriaImagenes.objects.filter(user__userprofile__contraparte = org).count()
		conteo_vid = GaleriaVideos.objects.filter(user__userprofile__contraparte = org).count()
		conteo_publi = Publicacion.objects.filter(usuario__userprofile__contraparte = org).count()

		list_resumen.append((org.siglas,conteo,conteo_eventos,conteo_foros,conteo_aportes,conteo_coment,conteo_img,conteo_vid,conteo_publi))

	return render(request, template, locals())