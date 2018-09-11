from django.contrib import admin

# Register your models here.
from .models import user_groups,user,doctor,Patient

admin.site.register(user_groups)  

admin.site.register(user)

admin.site.register(doctor)

admin.site.register(Patient)