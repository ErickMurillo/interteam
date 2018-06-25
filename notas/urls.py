from django.urls import include, path, re_path
from django.views.generic import ListView, DetailView
from .models import Notas
from .views import *

urlpatterns = [
    #url(r'^$', ListView.as_view(model=Notas, paginate_by=2, 
	#			  template_name="notas/notas_list.html"),
	#			  name='notas_list'),
    path('', lista_notas, name="notas_list"),
    # path('pais/(?P<id>\d+)/$', lista_notas_pais, name="notas_list"),
    # path('ver/(?P<id>\d+)/$', comentar_nota, name='comentar-nota'),
    #url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Notas, 
    #						   template_name='notas/notas_detail.html'),
     #                                           name='notas_detail'),
    path('<slug>/', detalle_notas, name='detalle-notas'),
    path('filtro/temas/<temas>/', filtro_temas, name='filtro-temas'),
    # path('crear/$', crear_nota, name="crear-nota"),
    # path('editar/<slug>/', editar_nota, name='editar-nota'),
    # path('borrar/(?P<id>\d+)/$', borrar_nota, name='borrar-nota'),
    ]