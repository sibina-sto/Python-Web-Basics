from django.shortcuts import render, redirect

from authapp.models import ProfileModel
from myplantapp import models, forms


def home_page(request):
    profile = ProfileModel.objects.first()
    context = {'profile': profile}

    return render(request, template_name='home-page.html', context=context)


def catalogue_page(request):
    plants = models.PlantModel.objects.all()
    context = {'plants': plants}

    return render(request, template_name='catalogue.html', context=context)


def create_plant_page(request):
    if request.method == 'POST':
        form = forms.PlantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = forms.PlantForm()

    context = {'form': form}

    return render(request, template_name='create-plant.html', context=context)


def plant_details_page(request, plant_id):
    plant = models.PlantModel.objects.get(id=plant_id)
    context = {'plant': plant}

    return render(request, template_name='plant-details.html', context=context)


def edit_plant_page(request, plant_id):
    plant = models.PlantModel.objects.get(id=plant_id)

    if request.method == "GET":
        context = {'form': forms.PlantForm(initial=plant.__dict__)}
        return render(request, 'edit-plant.html', context)
    else:
        form = forms.PlantForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, 'edit-plant.html', context)


def delete_plant_page(request, plant_id):
    plant = models.PlantModel.objects.get(id=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = forms.DeletePlantForm(instance=plant)
    context = {'form': form}

    return render(request, 'delete-plant.html', context)
