from django.contrib import admin
from .models import *
from django.forms import Textarea
import nested_admin

# Register your models here.

class ArchivoInline(nested_admin.NestedTabularInline):
	model = Archivo
	extra = 1

class InformeInline(nested_admin.NestedTabularInline):
	model = Informe
	extra = 1

class ImagenesInline(nested_admin.NestedTabularInline):
	model = Imagenes
	extra = 1

class VideoInline(nested_admin.NestedTabularInline):
	model = Video
	extra = 1

class DocumentoInline(nested_admin.NestedTabularInline):
	model = Documento
	extra = 1
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':35})},
	}

class HistoriasExitoInline(nested_admin.NestedTabularInline):
	model = HistoriasExito
	extra = 1
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':35})},
	}

class ArchivosMonitoreoInline(nested_admin.NestedTabularInline):
	model = ArchivosMonitoreo
	extra = 1

class MonitoreoInline(nested_admin.NestedTabularInline):
	model = Monitoreo
	extra = 1
	inlines = [ArchivosMonitoreoInline,]

class ProyectoAdmin(nested_admin.NestedModelAdmin):
	inlines = [ArchivoInline,InformeInline,ImagenesInline,VideoInline,DocumentoInline,MonitoreoInline]
	readonly_fields = ('url_para_compartir',)
	
	def get_queryset(self, request):
		if request.user.is_superuser:
			return Proyecto.objects.all()
		return Proyecto.objects.filter(user=request.user)
		
	def save_model(self, request, obj, form, change):
		if request.user.is_superuser:
			obj.save()
		else:
			obj.user = request.user
			obj.save()

	def get_form(self, request, obj=None, **kwargs):
		if not request.user.is_superuser:
			self.exclude = ('user',)
		else:
			self.exclude = ()
		return super(ProyectoAdmin, self).get_form(request, obj=None, **kwargs) 

admin.site.register(Proyecto,ProyectoAdmin)