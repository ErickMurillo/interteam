from django.shortcuts import render
from .models import *
from notas.models import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
import datetime

# Create your views here.
def list_eventos(request,template='events.html'):
	eventos = Agendas.objects.filter(publico = True).order_by('inicio')
	hoy = datetime.date.today()
	prox_eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).order_by('inicio')[:3]
	ultimas_notas = Notas.objects.order_by('-fecha','-id')[:4]

	return render(request, template, locals())

def detail_evento(request,slug,template="event-details.html"):
	evento = get_object_or_404(Agendas, slug=slug)
	hoy = datetime.date.today()
	prox_eventos = Agendas.objects.filter(inicio__gte = hoy, publico = True).exclude(slug = slug).order_by('inicio')[:3]
	ultimas_notas = Notas.objects.order_by('-fecha','-id')[:4]
	
	return render(request, template, locals())