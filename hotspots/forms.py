from django.forms import ModelForm

from .models import ModelHotspots


class FormHostpots(ModelForm):
    class Meta:
        model = ModelHotspots
        fields = ('title', 'category', 'description', 'lat', 'lng', 'user')
