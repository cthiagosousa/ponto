from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "username",
            "email",
        }

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"
