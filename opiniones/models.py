from django.db import models
from django.core.validators import MaxLengthValidator
from sorl.thumbnail import ImageField

# Create your models here.
class Ocupacion(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre
	class Meta:
		verbose_name = 'Ocupación'
		verbose_name_plural = 'Ocupaciones'

class Opiniones(models.Model):
	nombre = models.CharField(max_length=200)
	foto = ImageField(upload_to='opinion/',null=True, blank=True)
	ocupacion = models.ForeignKey(Ocupacion,on_delete=models.DO_NOTHING)
	opinion = models.TextField(validators=[MaxLengthValidator(500)])

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Opinión'
		verbose_name_plural = 'Opiniones'