import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('ADMIN', 'Admin'),
    ('USER', 'User')
)


class User(AbstractUser):
    """
    Model representing a user

    id: Unique identifier for the user
    is_active: Boolean. Designates whether this user should be treated as active
    username: Unique username for the user
    email: Email address of the user
    mobile_number: Mobile number of the user
    first_name: First name of the user
    last_name: Last name of the user
    created_date: Date of creation of the user
    updated_date: Date of last modification of the user
    role: Role of the user
    password: Password of the user
    """
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
    password = models.CharField(max_length=255)
