from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create_task(request):
    # create a task
    return Response('Task created')


@api_view(['POST'])
def assign_task(request):
    # assign task to a user
    return Response('Task assigned')


@api_view(['GET'])
def get_task_list_by_user(request):
    # fetch task list for a specific user and return
    return Response('Task list')
