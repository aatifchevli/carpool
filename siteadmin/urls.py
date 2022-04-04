from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'siteadmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_list',views.admin_list, name='admin_list'),
    path('vehicle_register',views.vehicle_register, name='vehicle_register')
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
