from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class BannerIndex(models.Model):
	titulo = models.CharField(max_length=50)
	texto = models.CharField(max_length=150)
	imagen = ImageField(upload_to='banner-index/',help_text='720x440')

	class Meta:
		verbose_name = 'Banner Index'
		verbose_name_plural = 'Banner Index'

	def __str__(self):
		return self.titulo

class BannerProposito(models.Model):
	imagen = ImageField(upload_to='banner-proposito/',help_text='340x180')

	class Meta:
		verbose_name = 'Banner proposito'
		verbose_name_plural = 'Banner proposito'

	def __str__(self):
		return 'Imagen %s' % (self.id)

class OrgCooperantes(models.Model):
	titulo = models.CharField(max_length=50)
	imagen = ImageField(upload_to='org-coop/')

	class Meta:
		verbose_name = 'Organización Cooperante'
		verbose_name_plural = 'Organizaciones Cooperantes'

	def __str__(self):
		return self.titulo
