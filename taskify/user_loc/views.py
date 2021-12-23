from django.shortcuts import render
from .serializers import UsersSerializer
from .models import mfy_users, mfy_task
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


def default_view(request):
    return HttpResponse("Welcome to Taskify World")


def users(request):
    if request.method == 'GET':
        users = mfy_users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_detail(request, task_id):
    if request.method == 'GET':
        users = mfy_users.objects.get(task_id=task_id)
        serializer = UsersSerializer(users)
        return JsonResponse(serializer.data)




def index(request):
    response = requests.get('http://127.0.0.1:8000/user_detail').json()
    return render(request, 'index.html', {'response': response})
