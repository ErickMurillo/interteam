from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Publicacion(models.Model):
	titulo = models.CharField(max_length=250)
	imagen = ImageField(upload_to='publicaciones/img/',null=True, blank=True)
	archivo = models.FileField(upload_to='publicaciones/archivos/')

	def __str__(self):
		return u'%s' % self.titulo

	class Meta:
		verbose_name_plural = 'Publicaciones'