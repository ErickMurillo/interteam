from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_catalogo, name='list-catalogo'),
    path('<id>/<slug>/', detalle_catalogo, name='detalle-catalogo'),
]
