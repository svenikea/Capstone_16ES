from django.urls import path, include
from .views import Task_Create, Task_Delete, Task_List, Task_Update, TaskViewSet, apiOverview, Task_Detail
from rest_framework import routers
#router = routers.DefaultRouter()
#router.register('Tasks' ,TaskViewSet)
app_name = "rest"
urlpatterns = [
	path('api-view/', apiOverview, name = "api_view"),
	#path('', include(router.urls), name = "list"),
	path('task_detail/<int:pk>/', Task_Detail, name = "task_detail"),
	path('task_delete/<int:pk>/', Task_Delete, name = "task_delete"),
	path('task_update/<int:pk>/', Task_Update, name = "task_update"),
	path('task_create/', Task_Create, name = "task_create"),
	path('task_list/', Task_List, name = "task_list"),
]