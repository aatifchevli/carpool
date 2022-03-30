from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('superuser_register', views.superuser_register, name='superuser_register'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
