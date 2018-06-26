from django.contrib import admin
from .models import *

# Register your models here.
class ArchivosAdmin(admin.ModelAdmin):
	def save_model(self,request,obj,form,change):
		obj.usuario = request.user
		obj.save()

admin.site.register(Archivos,ArchivosAdmin)