from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def assign_task(request):
    # assign task to a user
    return Response('Task assigned')