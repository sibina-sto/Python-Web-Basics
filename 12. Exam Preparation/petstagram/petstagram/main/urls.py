from django.urls import path

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.main.views.photos import CreatePetsPhotoView, PetsPhotoDetailsView, like_pet_photo, EditPetsPhotoView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/details/<int:pk>/', PetsPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', CreatePetsPhotoView.as_view(), name='create photo'),
    path('photo/edit/<int:pk>/', EditPetsPhotoView.as_view(), name='edit photo'),
)
