from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
# Create your views here.
from .models import TaskList, Games
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer



# An overall review of basic 
@api_view(['GET'])
def apiOverview(request):
	# This is a json return 
	api_url = {
	'List' : '/task-list/',
	'Create' : '/task-create/',
	'Update' : '/task-update/<int:id>/',
	'Delete' : '/task-delete/<int:id>',
	'Detail' : '/task-detail/<int:id>',
	
	}
	return Response(api_url)


# CRUD operations
# List all
@api_view(['GET'])
def Task_List(request):
	tasklist = TaskList.objects.all().order_by('-id')
	serializer = TaskSerializer(tasklist, many=True)
	return Response(serializer.data)


# Create
@api_view(['POST'])
def Task_Create(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return redirect("rest:task_list")
	return Response(serializer.data)

# Read
@api_view(['GET'])
def Task_Detail(request, pk):
	tasklist = get_object_or_404(TaskList, id=pk)
	serializer = TaskSerializer(tasklist, many=False)
	return Response(serializer.data)

# Update 
@api_view(['POST'])
def Task_Update(request, pk):
	tasklist = get_object_or_404(TaskList, id=pk)
	serializer = TaskSerializer(data=request.data, instance=tasklist)
	if serializer.is_valid():
		serializer.save()
		return redirect("rest:task_list")
	return Response(serializer.data)

# Delete
@api_view(['DELETE'])
def Task_Delete(request, id):
	tasklist = get_object_or_404(TaskList, id=id)
	tasklist.delete()
	return Response("rest:task_list")

#######################################################3
# Another shortcut of doing rest api
# Viewset method
class TaskViewSet(viewsets.ModelViewSet):
	queryset = TaskList.objects.all()
	serializer_class = TaskSerializer

# Using Traditional function-based view with rest api

