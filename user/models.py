import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True, 
        editable=False, 
        unique=True, 
        default=uuid.uuid4,
    )

    class Meta:
        db_table = "users"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("CustomUser_detail", kwargs={"pk": self.pk})