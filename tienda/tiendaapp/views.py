from django.shortcuts import render
from tiendaapp.models import Producto,Vendedor
from django.shortcuts import get_object_or_404
from tiendaapp.forms import anadircocheForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def indice(request):
   listacoches = Producto.objects.all().order_by('Precio')
   return render(request, 'tiendaapp/index.html', {'listacoches': listacoches })


def vendedor(request,vendedor_id):
	vendedor = get_object_or_404(Vendedor, pk = vendedor_id)
	return render(request, 'tiendaapp/detallevendedor.html', {'vendedor': vendedor })

@login_required
def anadircoche(request):
	if request.method == "POST":
		form = anadircocheForm(request.POST,request.FILES)
		if form.is_valid():
			receta = form.save()
			receta.save()
			return HttpResponseRedirect("/")
	else:
		form = anadircocheForm()
	return render(request, 'tiendaapp/anadircoche.html', {'form': form})

def caracteristicas(request,caracteristicas_id):
	caracteristicas = get_object_or_404(Producto, pk = caracteristicas_id)
	return render(request, 'tiendaapp/caracteristicas.html', {'caracteristicas': caracteristicas })

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
		form = AuthenticationForm()
	return render(request,'tiendaapp/login.html', {'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "tiendaapp/registro.html", {
'form': form,})





