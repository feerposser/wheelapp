from django.shortcuts import render, redirect, reverse

from .forms import FormHostpots
from .models import ModelCategories, ModelHotspots


def hotspots(request):
    if request.POST:
        form = FormHostpots(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("DEU RUIM", form.is_valid(), form.errors)

    categories = ModelCategories.objects.all()

    return render(request, 'hotspot.html', {"categories": categories})


def all_hotspots(request):
    return render(request, 'all_hotspots.html',
                  {"hotspots": ModelHotspots.objects.all()})


def routes(request):
    return render(request, 'routes.html')


def index(request):
    return redirect(hotspots)