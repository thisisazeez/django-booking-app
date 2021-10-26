from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUsers

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUsers
    list_display = ['email', 'username', 'age', 'is_staff', 'phone_number', 'address',]

admin.site.register(CustomUsers, CustomUserAdmin)
