from django.shortcuts import render
from .models import *
from notas.models import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
import datetime
from django.db.models import Q
from agendas.models import *
from django.http import HttpResponseRedirect, HttpResponse 
from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.
def list_eventos(request,template='events.html'):
	if request.GET.get('buscar'):
		q = request.GET['buscar']
		eventos = Agendas.objects.filter(Q(evento__icontains = q) |
										Q(descripcion__icontains = q) |
										Q(lugar__icontains = q), publico = True).order_by('inicio')
	else:
		eventos = Agendas.objects.filter(publico = True).order_by('inicio')

	hoy = datetime.date.today()
	prox_eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]
	ultimas_notas = Notas.objects.order_by('-fecha','-id')[:4]

	dic_eventos = {}
	for prox_event in prox_eventos:
		delta = datetime.datetime(year=prox_event.inicio.year,month=prox_event.inicio.month,day=prox_event.inicio.day,minute=prox_event.hora_inicio.minute) - datetime.datetime.now()
		days = delta.days
		hours = delta.seconds/3600
		dic_eventos[prox_event] = days,hours

	return render(request, template, locals())

def detail_evento(request,slug,template="event-details.html"):
	evento = get_object_or_404(Agendas, slug=slug)
	hoy = datetime.date.today()
	prox_eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).exclude(slug = slug).order_by('inicio')[:3]
	dic_eventos = {}
	for prox_event in prox_eventos:
		delta = datetime.datetime(year=prox_event.inicio.year,month=prox_event.inicio.month,day=prox_event.inicio.day,minute=prox_event.hora_inicio.minute) - datetime.datetime.now()
		days = delta.days
		hours = delta.seconds/3600
		dic_eventos[prox_event] = days,hours

	ultimas_notas = Notas.objects.order_by('-fecha','-id')[:4]

	# This gives timedelta in days & seconds
	delta = datetime.datetime(year=evento.inicio.year,month=evento.inicio.month,day=evento.inicio.day,minute=evento.hora_inicio.minute) - datetime.datetime.now()
	days = delta.days
	hours = delta.seconds/3600

	return render(request, template, locals())

import sys
def confirmar_evento(request, slug):
	user = UserProfile.objects.get(user__id = request.user.id)
	evento = Agendas.objects.get(slug = slug)
	email = evento.user.email
	list_mail = []
	list_mail.append(email)
	try:
		subject, from_email = 'Confirmación de participación en evento', 'cluster.nicaragua@gmail.com'
		text_content = 'El usuario '+ user.user.username +' de la Organización '+ str(user.contraparte) +' \n'  + \
						'ha confirmado la participación en el evento: "'+ evento.evento +'"'

		html_content = 'El usuario '+ user.user.username +' de la Organización '+ str(user.contraparte) +' \n'  + \
						'ha confirmado la participación en el evento: "'+ evento.evento +'"'

		msg = EmailMultiAlternatives(subject, text_content, from_email, list_mail)
		msg.attach_alternative(html_content, "text/html")
		msg.send()

		enviado = 1
		# return redirect('agenda-detail', slug=slug)
	except:
		pass

	return redirect('agenda-detail', slug=slug)