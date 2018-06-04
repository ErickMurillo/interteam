from django.urls import include, path, re_path
from django.views.generic import ListView, DetailView
from .models import Foros
from .views import *

urlpatterns = [
    #url(r'^$', 'index', name='index'),
    path('', ListView.as_view(model=Foros, 
    	                        template_name="foros/foro_list.html"),
    	                        name='foro-list'),
    #url(r'^$', 'lista_foro', name='lista-foro'), 
    # re_path(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Foros, 
    # 	                                        template_name='foros/foro_detail.html'),
    #                                             name='foro-detail'),
    # re_path(r'^crear/$', crear_foro, name='crear-foro'),
    # re_path(r'^editar/(?P<id>\d+)/$', editar_foro, name='editar-foro'),
    # re_path(r'^borrar/(?P<id>\d+)/$', borrar_foro, name='borrar-foro'),
    # re_path(r'^ver/(?P<foro_id>\d+)/$', ver_foro, name='ver-foro'),
    # re_path(r'^ver_comentario/(?P<aporte_id>\d+)/$', comentario_foro, name='cometario-foro'),
    # re_path(r'^privado/nota/$', notas_personales, name='notas-personales'),
    # re_path(r'^privado/agenda/$', agenda_personales, name='agenda-personales'),
    # re_path(r'^privado/documento/$', documento, name='documentos'),
    # re_path(r'^privado/documento_tag/(?P<tags>\w+)/$', busqueda_tag, name='busqueda-tag'),
    # re_path(r'^privado/multimedia_fotos/$', multimedia_fotos, name='multimedia_fotos'),
    # re_path(r'^privado/multimedia_fotos_tag/(?P<tags>\w+)/$', multimedia_fotos_tag, name='multimedia_fotos_tag'),
    # re_path(r'^privado/multimedia_videos/$', multimedia_videos, name='multimedia_videos'),
    # re_path(r'^privado/multimedia_videos_tag/(?P<tags>\w+)/$', multimedia_videos_tag, name='multimedia_videos_tag'),
    # re_path(r'^privado/multimedia_videos_sel/(?P<video>\w+)/$', multimedia_videos_sel, name='multimedia_videos_sel'),
    # re_path(r'^privado/multimedia_audios/$', multimedia_audios, name='multimedia_audios'),
    # re_path(r'^privado/multimedia_audios_tag/(?P<tags>\w+)/$', multimedia_audios_tag, name='multimedia_audios_tag'),    
    # re_path(r'^aporte/editar/(?P<aporte_id>\d+)/$', editar_aporte, name='editar-aporte'),
    # re_path(r'^aporte/borrar/(?P<id>\d+)/$', borrar_aporte, name='borrar-aporte'),
    # re_path(r'^comentario/editar/(?P<comen_id>\d+)/$', editar_comentario, name='editar-comentario'),
    # re_path(r'^comentario/borrar/(?P<id>\d+)/$', borrar_comentario, name='borrar-comentarios'),
]
