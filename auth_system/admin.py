from django.contrib import admin
from auth_system.models import CustomUser

#адмінка: admin пароль 1
admin.site.register(CustomUser)

