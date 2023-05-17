from django.urls import path
from myplantapp import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('catalogue/', views.catalogue_page, name='catalogue'),
    path('create/', views.create_plant_page, name='create-plant-page'),
    path('details/<int:plant_id>', views.plant_details_page, name='plant-details-page'),
    path('edit/<int:plant_id>', views.edit_plant_page, name='edit-plant-page'),
    path('delete/<int:plant_id>', views.delete_plant_page, name='delete-plant-page'),
]
