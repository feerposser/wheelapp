from rest_framework.viewsets import ModelViewSet

from hotspots.models import ModelHotspots
from .serializers import SerializerHotspots


class ViewsetHotspots(ModelViewSet):
    queryset = ModelHotspots.objects.all()
    serializer_class = SerializerHotspots
