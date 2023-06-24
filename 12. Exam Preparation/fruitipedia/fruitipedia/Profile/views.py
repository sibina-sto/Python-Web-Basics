from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from .models import Profile
from .forms import ProfileCreateForm, ProfileEditForm
from ..fruit.models import Fruit
from .helper import ProfileInfo


class ProfileCreate(views.CreateView):
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dashboard')


# class ProfileDetails(ProfileInfo, views.DetailView):
#     model = Profile
#     template_name = 'profile/details-profile.html'
#     extra_context = {'fruits_count': Fruit.objects.all().count()}


def profile_details(request):
    profile = Profile.objects.first()
    fruits_count = Fruit.objects.all().count()
    context = {
        'profile': profile,
        'fruits_count': fruits_count
    }
    return render(request, 'profile/details-profile.html', context)


class ProfileEdit(ProfileInfo, views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('profile-details')


class ProfileDelete(ProfileInfo, views.DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form = super().form_valid(form)
        Fruit.objects.all().delete()
        return form
