from rest_framework.serializers import ModelSerializer

from hotspots.models import ModelHotspots, ModelCategories


class SerializerCategories(ModelSerializer):
    class Meta:
        model = ModelCategories
        fields = ('name', 'description')


class SerializerHotspots(ModelSerializer):
    category = SerializerCategories()

    class Meta:
        model = ModelHotspots
        fields = ('title', 'category', 'description', 'lat', 'lng')
