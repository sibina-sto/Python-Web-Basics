from django.shortcuts import render, redirect

from authapp.forms import EditProfileForm, ProfileForm
from authapp.models import ProfileModel
from myplantapp.models import PlantModel


def profile_details_page(request):
    profile = ProfileModel.objects.first()
    all_plants = len(PlantModel.objects.all())

    context = {
        'profile': profile,
        'all_plants': all_plants
    }

    return render(request, template_name='profile-details.html', context=context)


def create_profile_page(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {'form': form}

    return render(request, template_name='create-profile.html', context=context)


def edit_profile_page(request):
    profile = ProfileModel.objects.first()

    if request.method == "GET":
        context = {'form': EditProfileForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('profile-details-page')
        else:
            context = {'form': form}

            return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = ProfileModel.objects.first()
    plants = PlantModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()

        return redirect('home-page')

    return render(request, 'delete-profile.html')
