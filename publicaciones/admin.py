from django.contrib import admin
from .models import *

# Register your models here.
class ArchivosPublicacionInline(admin.TabularInline):
	model = ArchivosPublicacion
	extra = 1

class AudiosPublicacionInline(admin.TabularInline):
	model = AudiosPublicacion
	extra = 1

class VideosPublicacionInline(admin.TabularInline):
	model = VideosPublicacion
	extra = 1

class PublicacionAdmin(admin.ModelAdmin):
	inlines = [ArchivosPublicacionInline,AudiosPublicacionInline,VideosPublicacionInline]
	
	# def save_model(self,request,obj,form,change):
	# 	obj.usuario = request.user
	# 	obj.save()

admin.site.register(Publicacion,PublicacionAdmin)
