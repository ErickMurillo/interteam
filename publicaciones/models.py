from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User 

# Create your models here.
class Publicacion(models.Model):
	titulo = models.CharField(max_length=250)
	imagen = ImageField(upload_to='publicaciones/img/',null=True, blank=True)
	archivo = models.FileField(upload_to='publicaciones/archivos/')
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,editable=False)

	def __str__(self):
		return u'%s' % self.titulo

	class Meta:
		verbose_name_plural = 'Publicaciones'