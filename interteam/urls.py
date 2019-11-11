"""interteam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from notas import views as notas
from contrapartes import views as contra
from foros.views import *
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Administración Cluster'
admin.site.site_title = 'Cluster'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('nested_admin/', include('nested_admin.urls')),
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/profile/', perfil, name='perfil'),
    path('accounts/profile/editar/', contra.perfil_editar, name='perfil_editar'),
    path('accounts/logout/', notas.logout_page, name='logout'),
    path('accounts/password_reset/', auth_views.password_reset, name='password_reset'),
    path('accounts/password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('', notas.index),
    path('notas/', include('notas.urls')),
    path('contrapartes/', include('contrapartes.urls')),
    path('eventos/', include('agendas.urls')),
    path('foros/', include('foros.urls')),
    path('galerias/', include('galerias.urls')),
    path('publicaciones/', notas.publicaciones),
    path('publicaciones/<slug>', notas.publicacion_detalle, name='publicacion-detalle'),
    path('publicaciones/filtro/tema/<tema>', notas.filtro_temas_publi, name='filtro-temas-publi'),
    path('organizaciones/', notas.organizaciones),
    path('organizaciones/<slug>', notas.detalle_organizacion, name='detalle-organizacion'),
    path('biblioteca/', include('biblioteca.urls')),
    path('contacto/', notas.contacto, name='contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
