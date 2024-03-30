
from django.contrib import admin
from django.urls import path
from mainApp_2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fan/', fanlar)
]
