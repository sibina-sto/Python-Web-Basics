from django.shortcuts import render, redirect

from .models import Car
from .forms import CarCreateForm, CarEditForm, CarDeleteForm


def car_create(request):
    form = CarCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'car/car-create.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    form = CarEditForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-edit.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context)
