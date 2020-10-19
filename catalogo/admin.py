from django.contrib import admin
from .models import *

# Register your models here.

class Propuesta_valor_Inline(admin.TabularInline):
    model = Propuesta_valor
    extra = 1

class FotosProducto_Inline(admin.TabularInline):
    model = FotosProducto
    extra = 1
    max_num = 4

class ArchivosProducto_Inline(admin.TabularInline):
    model = ArchivosProducto
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = [Propuesta_valor_Inline,FotosProducto_Inline,ArchivosProducto_Inline]

admin.site.register(TipoProducto)
admin.site.register(ServiciosProducto)
admin.site.register(Producto,ProductoAdmin)
