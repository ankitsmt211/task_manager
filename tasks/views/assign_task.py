from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.models import Task
from users.models import User


@api_view(['POST'])
def assign_task(request, *args, **kwargs):
    user_id = kwargs.get('user_id')
    task_id = kwargs.get('task_id')
    if not user_id or not task_id:
        return Response(data='Bad URL', status=status.HTTP_400_BAD_REQUEST)
    user_obj = User.objects.filter(id=user_id).first()
    if not user_obj:
        return Response(data='Invalid User ID', status=status.HTTP_400_BAD_REQUEST)

    task_obj = Task.objects.filter(id=task_id).first()
    if not task_obj:
        return Response(data='Invalid Task ID', status=status.HTTP_400_BAD_REQUEST)

    task_obj.users.add(user_obj)

    return Response('Task assigned to user', status=status.HTTP_200_OK)
