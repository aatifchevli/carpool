from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'siteadmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_list',views.admin_list, name='admin_list'),
    path('vehicle_register',views.vehicle_register, name='vehicle_register'),
    path('create_siteadmin', views.create_siteadmin, name="create_siteadmin"),
    path('create_poolhost', views.create_poolhost, name="create_poolhost"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
