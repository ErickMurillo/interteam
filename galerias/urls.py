from django.urls import include, path, re_path
from .models import *
from .views import *

urlpatterns = [
	path('imagenes/', lista_galerias_img, name='lista-galerias-img'),
	path('imagenes/<id>/', detalle_galerias_img, name='detalle-galerias-img'),
	path('videos/', lista_galerias_videos, name='lista-galerias-videos'),
	path('videos/<id>/', detalle_galerias_video, name='detalle-galerias-video'),
]