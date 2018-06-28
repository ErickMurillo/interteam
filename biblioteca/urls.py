from django.urls import include, path
from .views import *

urlpatterns = [
	path('', list_biblioteca, name='list_biblioteca'),
	path('<slug>/', detail_biblioteca, name='biblioteca-detail'),
	]