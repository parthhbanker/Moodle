from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # default admin page
    path('admin/', include('admin.urls')),
    path('', include('admin.urls'))
]
