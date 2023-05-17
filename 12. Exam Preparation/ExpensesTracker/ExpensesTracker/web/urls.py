from django.urls import path

from ExpensesTracker.web.views import show_index, create_expense, edit_expense, delete_expense, show_profile, \
    create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_index, name='index'),
    path('expenses/create/', create_expense, name='create expense'),
    path('expenses/edit/<int:pk>/', edit_expense, name='edit_expense'),
    path('expenses/delete/<int:pk>/', delete_expense, name='delete expense'),
    path('profile/', show_profile, name='show profile'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
