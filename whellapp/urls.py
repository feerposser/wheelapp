
from django.contrib import admin
from django.urls import path, include

from hotspots.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotspots/', hotspots),
    path('', index),
    path('all_hotspots/', all_hotspots),
    path('routes/', routes),
    path('api/', include('whellapp.urls_api'))
]
