from django.urls import path

from Notes_App.web.views import show_index, add_note, edit_note, delete_note, show_details, show_profile, \
    create_profile, delete_profile

urlpatterns = (
    path('', show_index, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', show_details, name='show details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
