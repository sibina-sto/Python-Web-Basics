from django.urls import path, include

from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
    path('game/', include([
        path('create/', views.game_create, name='game_create'),
        path('details/<int:pk>/', views.game_details, name='game_details'),
        path('edit/<int:pk>/', views.game_edit, name='game_edit'),
        path('delete/<int:pk>/', views.game_delete, name='game_delete'),
    ])),
)
