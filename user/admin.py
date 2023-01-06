from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomChangeForm, CustomCreationForm
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm
    model = User
    list_display = ("email", "name", "is_active")
