from django.urls import path

from tasks.views import create_task, assign_task, get_task_list_by_user

urlpatterns = [
    path('api/v1/task/', create_task),
    path('api/v1/user/<uuid:user_id>/task/assign/', assign_task),
    path('api/v1/user/<uuid:user_id>/task/list/', get_task_list_by_user)
]
