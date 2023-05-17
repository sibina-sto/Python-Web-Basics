from django.urls import path
from car_collection.auth_app.views import create_profile_page, edit_profile_page, delete_profile_page, profile_details_page


urlpatterns = [
    path('create/', create_profile_page, name='create-profile'),
    path('edit/', edit_profile_page, name='edit-profile'),
    path('delete/', delete_profile_page, name='delete-profile'),
    path('details/', profile_details_page, name='profile-details'),
]
