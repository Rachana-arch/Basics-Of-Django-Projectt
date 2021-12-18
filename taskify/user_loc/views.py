from django.shortcuts import render
from .serializers import UsersSerializer
from .models import mfy_users, mfy_task
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


def user_detail(request, task_id):
    # users = mfy_users.objects.all()
    try:
        users = mfy_users.objects.get(task_id=task_id)
    except users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return JsonResponse(serializer.data)


def index(request):
    response = requests.get('http://127.0.0.1:8000/user_detail').json()
    return render(request, 'index.html', {'response': response})
