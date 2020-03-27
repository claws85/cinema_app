from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserChangeForm
