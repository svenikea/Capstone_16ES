from rest_framework import serializers
from .models import TaskList

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskList
		fields = '__all__'