from django.urls import path

from car_collection.common.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
