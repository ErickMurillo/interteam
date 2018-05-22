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
from foros.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('accounts/login/', auth_views.login),
    path('accounts/profile/',perfil,name='perfil'),
    path('accounts/logout/', notas.logout_page),
    path('password_change/',auth_views.password_change,
                            {'template_name': 'registration/password_change_form.html',
                            'post_change_redirect': '/foros/perfil/'},
                            name='password-change'),
    path('', notas.index),
    path('notas/', include('notas.urls')),
    # path('contrapartes/', include('contrapartes.urls')),
    path('eventos/', include('agendas.urls')),
    path('foros/', include('foros.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
