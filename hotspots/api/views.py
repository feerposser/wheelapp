from rest_framework.views import APIView
from rest_framework.response import Response

from hotspots.models import ModelHotspots


class ListLatLng(APIView):
    def get(self, request, format=None):
        hotspots = []
        for hotspot in ModelHotspots.objects.all():
            hotspots.append({'lat': hotspot.lat,
                             'lng': hotspot.lng})

        return Response(hotspots, status=200)
