from django.urls import path

from GamesPlay_App.web.views import show_index, show_dashboard, create_game, show_game_details, edit_game, delete_game, \
    create_profile, show_profile_details, edit_profile, delete_profile

urlpatterns = (
    path('', show_index, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', show_game_details, name='game details'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', show_profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
