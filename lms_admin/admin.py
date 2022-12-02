from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CategoryModel)
admin.site.register(CourseModel)
admin.site.register(AdminModel)
admin.site.register(WebSettingModel)