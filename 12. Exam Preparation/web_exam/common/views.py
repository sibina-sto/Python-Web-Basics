from django.shortcuts import render

from ..car.models import Car
from ..car_profile.models import Profile


def index(request):
    return render(request, 'common/index.html', )


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    context = {
        'cars': cars,
        'profile': profile
    }
    return render(request, 'common/catalogue.html', context)
