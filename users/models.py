import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('ADMIN', 'Admin'),
    ('USER', 'User')
)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
