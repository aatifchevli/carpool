from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'poolhost'

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicle_register', views.vehicle_register, name='vehicle_register'),
    path('VehicleType', views.VehicleType, name='VehicleType')
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
