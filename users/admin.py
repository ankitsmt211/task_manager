from django.contrib import admin

from users.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'role')
    exclude = ['created_at', 'updated_at']


admin.site.register(User, UserAdmin)
