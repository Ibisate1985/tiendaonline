from django.db import models

# Create your models here.



class Vendedor(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)


class Producto (models.Model):
	Marca = models.CharField(max_length=30)
	Vendedor = models.ForeignKey(Vendedor,default=1)
	Modelo = models.CharField(max_length=30)
	Combustible = models.CharField(max_length=30)
	Precio = models.CharField(max_length=30)
	Video  = models.TextField(max_length=300,default='1')
	foto = models.ImageField(null=True, upload_to='tiendaapp/static/media')

def __str__(self):
		return '%s' % (self.nombre)







	
