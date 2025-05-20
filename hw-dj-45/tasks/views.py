from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
