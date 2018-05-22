from django.shortcuts import render
from .models import *

# Create your views here.
def list_eventos(request,template='events.html'):
	eventos = Agendas.objects.filter(publico = True).order_by('inicio')

	return render(request, template, locals())