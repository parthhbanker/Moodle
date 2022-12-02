from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('def_admin/',  admin.site.urls),
    # default admin page
    path('admin/', include('lms_admin.urls')),
    path('', include('lms_admin.urls'))
]
