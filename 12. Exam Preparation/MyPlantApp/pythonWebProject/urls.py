from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myplantapp.urls')),
    path('account/', include('authapp.urls')),
]
