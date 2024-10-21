from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create_task(request):
    # create a task
    return Response('Task created')