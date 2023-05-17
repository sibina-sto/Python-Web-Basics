from django.shortcuts import render, redirect

from car_collection.auth_app.models import Profile
from car_collection.cars_app.forms import DeleteCarForm, CarForm
from car_collection.cars_app.models import Car


def catalogue_page(request):
    cars = Car.objects.all()
    context = {
        'profile': Profile.objects.first(),
        'cars': cars
    }

    return render(request, template_name='catalogue.html', context=context)


def create_car_page(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('catalogue')

    context = {
        'profile': Profile.objects.first(),
        'form': form
    }

    return render(request, template_name='create-car.html', context=context)


def car_details_page(request, pk):
    car = Car.objects.get(id=pk)
    context = {
        'profile': Profile.objects.first(),
        'car': car
    }

    return render(request, template_name='car-details.html', context=context)


def edit_car_page(request, pk):
    car = Car.objects.get(id=pk)

    if request.method == "GET":
        context = {
            'profile': Profile.objects.first(),
            'form': CarForm(initial=car.__dict__)
        }
        return render(request, 'edit-car.html', context)

    else:
        form = CarForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {
                'profile': Profile.objects.first(),
                'form': form
            }
            return render(request, 'edit-car.html', context)


def delete_car_page(request, pk):
    car = Car.objects.get(id=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(instance=car)
    context = {
        'profile': Profile.objects.first(),
        'form': form
    }

    return render(request, 'delete-car.html', context)
