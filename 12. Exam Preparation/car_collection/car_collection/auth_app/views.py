from django.shortcuts import render, redirect

from car_collection.auth_app.forms import ProfileForm, EditProfileForm
from car_collection.auth_app.models import Profile
from car_collection.cars_app.models import Car


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


def profile_details_page(request):
    profile = Profile.objects.first()
    all_cars = Car.objects.all()
    total_sum = sum(car.price for car in all_cars)
    context = {'profile': profile, 'total_sum': total_sum}

    return render(request, template_name='profile-details.html', context=context)


def edit_profile_page(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {'form': EditProfileForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')
        else:
            context = {
                'profile': Profile.objects.first(),
                'form': form
            }
            return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()

        return redirect('home')

    return render(request, 'delete-profile.html', {"profile": Profile.objects.first()})
