from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Admin panelinde görünmesini istediğimiz alanlar
    list_display = ('username', 'email', 'balance')

admin.site.register(CustomUser, CustomUserAdmin)