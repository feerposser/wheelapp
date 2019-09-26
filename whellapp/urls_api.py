from django.urls import path, include
from rest_framework import routers

from hotspots.api.viewsets import ViewsetHotspots
from hotspots.api.views import ListLatLng

router = routers.DefaultRouter()
router.register(r'hotspots', ViewsetHotspots, base_name="HotspotViewSet")

urlpatterns = [
    path('', include(router.urls)),
    path('hotspots_lat_lng/', ListLatLng.as_view())
]
