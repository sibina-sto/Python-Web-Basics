from django.urls import path

from .views import car_create, car_edit, car_details, car_delete

urlpatterns = [
    path('create/', car_create, name='car-create'),
    path('<int:pk>/details/', car_details, name='car-details'),
    path('<int:pk>/edit/', car_edit, name='car-edit'),
    path('<int:pk>/delete/', car_delete, name='car-delete'),
]
