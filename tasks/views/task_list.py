from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def get_task_list_by_user(request):
    # fetch task list for a specific user and return
    return Response('Task list')