from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.models import Task


class SerializerTask(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ['created_at']


@api_view(['POST'])
def create_task(request, *args, **kwargs):
    """
    POST view to create a new task.
    :param request: The request object containing the task data.
    :param args: Additional positional arguments.
    :param kwargs: Additional keyword arguments.
    :return: Response with task data or errors.
    """
    serializer = SerializerTask(data=request.data)
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
