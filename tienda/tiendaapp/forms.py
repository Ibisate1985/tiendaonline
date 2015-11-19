from django import forms
from tiendaapp.models import Producto

class anadircocheForm(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ('Marca','Vendedor','Modelo','Combustible','Precio',)
