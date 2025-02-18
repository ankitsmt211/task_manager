# Generated by Django 5.1.2 on 2024-10-21 18:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('task_type', models.CharField(blank=True, max_length=50, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('TODO', 'Todo'), ('PENDING', 'Pending'), ('IN-PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='PENDING', max_length=50, null=True)),
            ],
        ),
    ]
