from django.contrib import admin
from django.conf.urls import include,url

urlpatterns = [
    # Examples:
    # url(r'^$', 'tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	 url(r'', include('tiendaapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
