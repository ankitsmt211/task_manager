from django.urls import path

from tasks.views.assign_task import assign_task
from tasks.views.create_task import create_task
from tasks.views.task_list import get_task_list_by_user

urlpatterns = [
    path('api/v1/task/', create_task),
    path('api/v1/user/<uuid:user_id>/task/<uuid:task_id>/assign/', assign_task),
    path('api/v1/user/<uuid:user_id>/task/list/', get_task_list_by_user)
]
