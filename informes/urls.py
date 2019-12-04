from django.urls import path
from .models import *
from .views import *

urlpatterns = [
	path('<slug>/', detalle_informe, name='detalle-informe'),
	path('<slug>/informes/', lista_informes, name='lista-informes'),
	path('<slug>/documentos/', lista_documentos, name='lista-documentos'),
	path('<slug>/imagenes/', imagenes, name='imagenes'),
	path('<slug>/videos/', videos, name='videos'),
]