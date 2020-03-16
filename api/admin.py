from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api import models

# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Source)
admin.site.register(models.Status)
admin.site.register(models.Hospital)
admin.site.register(models.Gender)
admin.site.register(models.Patient)
admin.site.register(models.Province)
admin.site.register(models.City)
admin.site.register(models.Laboratory)