import uuid
from datetime import timezone, datetime

from django.db import models

from users.models import User

STATUS_CHOICES = (
    ('TODO', 'Todo'),
    ('PENDING', 'Pending'),
    ('IN-PROGRESS', 'In Progress'),
    ('COMPLETED', 'Completed'),
)


class Task(models.Model):
    """
    Model representing a task.

    id: Unique task identifier
    name: Task name
    description: Task description
    created_at: Creation date
    task_type: Task type
    completed_at: Completion date
    status: Task status
    users: Users who are assigned to this task
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField()
    task_type = models.CharField(null=True, blank=True, max_length=50)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(default='TODO', choices=STATUS_CHOICES, null=True, blank=True, max_length=50)
    users = models.ManyToManyField(User, related_name='tasks', blank=True)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now(timezone.utc)
        return super(Task, self).save(*args, **kwargs)

