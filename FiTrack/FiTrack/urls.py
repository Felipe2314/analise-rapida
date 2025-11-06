# FiTrack/urls.py

from django.contrib import admin
from django.urls import path, include
# Importe a sua nova view aqui
from aplication.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('aplication.urls')),
    path('', home_page, name='home'),
]