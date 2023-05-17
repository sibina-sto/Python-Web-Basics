from django.urls import path
from authapp import views

urlpatterns = [
    path('create/', views.create_profile_page, name='create-profile-page'),
    path('details/', views.profile_details_page, name='profile-details-page'),
    path('edit/', views.edit_profile_page, name='edit-profile-page'),
    path('delete/', views.delete_profile_page, name='delete-profile-page'),
]
