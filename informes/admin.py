from django.contrib import admin
from .models import *
# Register your models here.

class ArchivoInline(admin.TabularInline):
	model = Archivo
	extra = 1

class InformeInline(admin.TabularInline):
	model = Informe
	extra = 1

class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1

class HistoriasExitoInline(admin.TabularInline):
	model = HistoriasExito
	extra = 1

class ProyectoAdmin(admin.ModelAdmin):
	inlines = [ArchivoInline,InformeInline,ImagenesInline,VideoInline,HistoriasExitoInline]
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