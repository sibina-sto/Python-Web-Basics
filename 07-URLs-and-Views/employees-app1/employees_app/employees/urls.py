from django.urls import path

from employees_app.employees.views import \
    department_details, \
    list_departments, not_found, create_department

urlpatterns = (
    path('create/', create_department),
    path('<str:id>/', department_details, name='department details'),
    path('', list_departments, name='list departments'),
    path('filter/by/order/', list_departments, name='custom url'),
    path('not-found/', not_found),
)