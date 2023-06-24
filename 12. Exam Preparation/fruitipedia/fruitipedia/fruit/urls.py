from django.urls import path, include

from .views import FruitCreate, FruitEdit, FruitDetails, FruitDelete

urlpatterns = [
    path('create/', FruitCreate.as_view(), name='fruit-create'),
    path('<int:pk>/', include([
        path('edit/', FruitEdit.as_view(), name='fruit-edit'),
        path('details/', FruitDetails.as_view(), name='fruit-details'),
        path('delete/', FruitDelete.as_view(), name='fruit-delete'),
    ]))
]
