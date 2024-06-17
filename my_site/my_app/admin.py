from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


admin.site.register(CustomUser, UserAdmin)
