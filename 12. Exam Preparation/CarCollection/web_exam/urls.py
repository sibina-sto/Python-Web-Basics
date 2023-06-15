from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_exam.common.urls')),
    path('car/', include('web_exam.car.urls')),
    path('profile/', include('web_exam.car_profile.urls')),
]
