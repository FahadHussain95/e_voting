from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'candidate_nic')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('candidate_nic', 'has_voted',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)