from django.urls import include, path, re_path
from .models import *
from .views import *

urlpatterns = [
	path('editar/<slug>/', editar_contraparte, name='editar-contraparte'),
	# path('notas/', notas_contraparte, name='notas-contraparte'),
]
