from django.urls import path

from .views import ProfileCreate, ProfileEdit, profile_details, ProfileDelete

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name='profile-create'),
    path('details/', profile_details, name='profile-details'),
    path('edit/', ProfileEdit.as_view(), name='profile-edit'),
    path('delete/', ProfileDelete.as_view(), name='profile-delete'),
]
