from django.contrib import admin

from tasks.models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    exclude = ['created_at']
    raw_id_fields = ('users',)


admin.site.register(Task, TaskAdmin)
