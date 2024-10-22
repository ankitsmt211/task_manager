from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.models import Task
from users.models import User


class SerializerTaskList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


@api_view(['GET'])
def get_task_list_by_user(request, *args, **kwargs):
    """
    GET view to return list of all tasks for a given user
    :param request: The request object containing the task data.
    :param args: Additional positional arguments.
    :param kwargs: Additional keyword arguments.
    :return: Response with task list or errors.
    """
    # fetch task list for a specific user and return
    user_id = kwargs.get('user_id')
    if not user_id:
        return Response(data='Bad URL', status=status.HTTP_400_BAD_REQUEST)

    user_obj = User.objects.filter(pk=user_id).first()
    if not user_obj:
        return Response(data='Invalid User ID', status=status.HTTP_400_BAD_REQUEST)
    serializer = SerializerTaskList(instance=user_obj.tasks, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
