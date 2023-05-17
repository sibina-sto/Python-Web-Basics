from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from petstagram.acounts.forms import CreateProfileForm
from petstagram.acounts.models import Profile
from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import Pet, PetsPhoto


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'acounts/profile_create.html'

    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'acounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView:
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'acounts/change_password.html'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'acounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user_id=self.object.user_id))
        pet_photos = PetsPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_images_count = len(pet_photos)
        total_likes_count = sum(pp.likes for pp in pet_photos)

        context.update({
            'total_images_count': total_images_count,
            'total_likes_count': total_likes_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })

        return context


# def show_profile(request):
#     profile = get_profile()
#     pets = list(Pet.objects.filter(user_profile=profile))
#     pet_photos = PetsPhoto.objects.filter(tagged_pets__in=pets).distinct()
#     total_images_count = len(pet_photos)
#     total_likes_count = sum(pp.likes for pp in pet_photos)
#     context = {
#         'profile': profile,
#         'total_images_count': total_images_count,
#         'total_likes_count': total_likes_count,
#         'pets': pets
#     }
#     return render(request, 'main/profile_details.html', context)


# def profile_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         form = form_class(instance=instance)
#
#     context = {
#         'form': form,
#     }
#     return render(request, template_name, context)


# def create_profile(request):
#     return profile_action(request, CreateProfileForm, 'index', Profile(), 'main/profile_create.html')
#
#
# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile', get_profile(), 'main/profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')


# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CreateProfileForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile_create.html', context)
#
#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = EditProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile_edit.html', context)
