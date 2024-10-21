import uuid

from django.db import models

from users.models import User

STATUS_CHOICES = (
    ('TODO', 'Todo'),
    ('PENDING', 'Pending'),
    ('IN-PROGRESS', 'In Progress'),
    ('COMPLETED', 'Completed'),
)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField()
    task_type = models.CharField(null=True, blank=True, max_length=50)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(default='PENDING', choices=STATUS_CHOICES, null=True, blank=True, max_length=50)
    users = models.ManyToManyField(User, related_name='tasks')
