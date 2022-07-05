from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


class ListTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET', 'POST'])
def list_all_tasks(request):
    try:
        tasks = Task.objects.all()
    except Task.DoesNotExist as e:
        return JsonResponse([], safe=False)
    if request.method == 'GET':
        serializer = TaskSerializer(tasks, many=True)
        tasks_list = []
        for task in serializer.data:
            tasks_list.append({
                'id': task['id'],
                'title': task['title'],
                'deadline': task['deadline'],
                'done': task['done'],
            })
        return Response(tasks_list)
    elif request.method == 'POST':
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PATCH', 'DELETE'])
def get_task(request, pk):
    try:
        task = Task.objects.filter(pk=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method == 'GET':
        serializer = TaskDetailSerializer(task, many=True)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        Task.objects.filter(pk=pk).update(type=request.data)
        task.save()
        return JsonResponse({'status': 'OK'})
    elif request.method == 'DELETE':
        task.delete()
        task.save()
        return JsonResponse({'status': 'OK'})


@api_view(['POST'])
def click_done(request, pk):
    try:
        task = Task.objects.filter(pk=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method == 'POST':
        task.done = True
        task.save()
        return JsonResponse({'status': 'OK'})
