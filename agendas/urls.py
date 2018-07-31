from django.urls import include, path, re_path
from django.views.generic import ListView, DetailView
from .models import Agendas
from .views import *

urlpatterns = [
	path('', list_eventos, name='list_eventos'),
	path('<slug>/', detail_evento,name='agenda-detail'),
	path('confirmar/<id>/', confirmar_evento, name='confirmar-evento'),
	# path('crear/', crear_agenda, name="crear-agenda"),
	# re_path(r'^editar/(?P<id>\d+)/$', editar_agenda, name='editar-agenda'),
	# re_path(r'^borrar/(?P<id>\d+)/$', borrar_agenda, name='borrar-agenda'),
	# path('calendario/', calendario, name='calendario'),
	# re_path(r'^calendario/(?P<id>\d+)/$', calendario, name='calendario'),
	# re_path(r'^eventos/(?P<id>\d+)/$', calendario_publico, name='calendario_publico'),
	# path('eventos/', calendario_publico, name='calendario_publico'),
	# path('calendar/', calendario_full_contraparte, name='calendario-full-contraparte'),
	# re_path(r'^calendar/(?P<id>\d+)/$', calendario_full_contraparte, name='calendario-full-contraparte'),
	]