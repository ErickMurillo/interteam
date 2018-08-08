from django.urls import include, path
from .views import *

urlpatterns = [
	path('', list_biblioteca, name='list_biblioteca'),
	path('<slug>/', detail_biblioteca, name='biblioteca-detail'),
	path('filtro/tema/<tema>/', filtro_tema_biblioteca, name='filtro-tema-biblioteca'),
	path('filtro/categoria/<categoria>/', filtro_categoria_biblioteca, name='filtro-categoria-biblioteca'),
	]