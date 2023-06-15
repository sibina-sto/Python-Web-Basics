from django.shortcuts import render, redirect

from .models import Profile
from ..car.models import Car
from .forms import ProfileCreateForm, ProfileEditForm


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)
    context = {
        'total_price': total_price
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form
    }
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')
