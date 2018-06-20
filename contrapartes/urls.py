from django.urls import include, path, re_path
from .models import *
from .views import *

urlpatterns = [
	path('editar/<slug>/', editar_contraparte, name='editar-contraparte'),
	path('notas/', notas_contraparte, name='notas-contraparte'),
	path('notas/redactar/', redactar_notas_contraparte, name='redactar-notas-contraparte'),
	path('notas/filtro/temas/<temas>/', filtro_temas_contra, name='filtro-temas-contra'),
	path('notas/eliminar/<slug>', eliminar_notas_contraparte, name='eliminar-notas-contraparte'),
	path('notas/editar/<slug>/', editar_nota, name='editar-nota'),
	path('eventos/', eventos_contraparte, name='eventos-contraparte'),
	path('eventos/nuevo/', nuevo_evento_contraparte, name='nuevo-evento-contraparte'),
	path('eventos/eliminar/<slug>', eliminar_evento_contraparte, name='eliminar-evento-contraparte'),
	path('eventos/editar/<slug>/', editar_evento, name='editar-evento'),
	path('foros/', list_foros, name='list-foros'),
	path('foros/eliminar/<id>', eliminar_foro, name='eliminar-foro'),
	path('foros/editar/<id>/', editar_foro, name='editar-foro'),
	path('foros/ver/<id>/', ver_foro, name='ver-foro'),
	path('foros/agregar/',agregar_foro, name='agregar-foro'),
	path('publicaciones/', publicaciones_contraparte, name='publicaciones-contraparte'),
	path('publicaciones/eliminar/<id>', eliminar_publicacion, name='eliminar-publicacion'),
	path('publicaciones/editar/<id>/', editar_publicacion, name='editar-publicacion'),
	path('publicaciones/agregar/',agregar_publicacion, name='agregar-publicacion'),
]
