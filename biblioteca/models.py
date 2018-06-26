from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User 

# Create your models here.
class Archivos(models.Model):
	titulo = models.CharField(max_length=250)
	imagen = ImageField(upload_to='biblioteca/img/',null=True, blank=True)
	archivo = models.FileField(upload_to='biblioteca/archivos/')
	usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,editable=False)

	def __str__(self):
		return u'%s' % self.titulo

	class Meta:
		verbose_name_plural = 'Archivos'