from django.conf.urls import url
from tiendaapp import views

urlpatterns = [
    url(r'^$', views.indice, name='indice'),
	 url(r'^vendedor/(?P<vendedor_id>\d+)/$',views.vendedor, name='vendedor'),
	 url(r'^anadircoche$',views.anadircoche, name='anadircoche'),
	 url(r'^caracteristicas/(?P<caracteristicas_id>\d+)/$',views.caracteristicas, name='caracteristicas'),
	 url(r'^registro$', views.registro, name='registro'),
 	 url(r'^login$', views.loginpage, name='login'),
    url(r'^logout$', views.logoutpage, name='logout'),
	 url(r'^anadircoche$', views.anadircoche, name='anadircoche')
	 
]
