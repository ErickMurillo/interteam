from django.contrib import admin
from .models import *

# Register your models here.
class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

class GaleriaImagenesAdmin(admin.ModelAdmin):
	inlines = [ImagenesInline,]

class VideosInline(admin.TabularInline):
	model = Videos
	extra = 1

class GaleriaVideosAdmin(admin.ModelAdmin):
	inlines = [VideosInline,]

admin.site.register(GaleriaImagenes, GaleriaImagenesAdmin)
admin.site.register(GaleriaVideos, GaleriaVideosAdmin)
admin.site.register(Tematica)