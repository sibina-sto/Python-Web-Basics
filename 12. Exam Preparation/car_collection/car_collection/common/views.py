from django.shortcuts import render

from car_collection.auth_app.models import Profile


def home_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name='index.html', context=context)
