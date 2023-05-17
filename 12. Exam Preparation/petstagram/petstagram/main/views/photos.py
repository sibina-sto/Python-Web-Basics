from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.models import PetsPhoto


# def show_photo_details(request, pk):
#     pet_photo = PetsPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
#     context = {
#         'pet_photo': pet_photo,
#     }
#     return render(request, 'main/photo_details.html', context)


class PetsPhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = PetsPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


class CreatePetsPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = PetsPhoto
    template_name = 'main/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetsPhotoView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = PetsPhoto
    template_name = 'main/photo_edit.html'
    fields = ('description', 'tagged_pets')

    def get_success_url(self, **kwargs):
        return reverse_lazy('pet photo details', kwargs={'pk': self.object.id})


def like_pet_photo(request, pk):
    pet_photo = PetsPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)
