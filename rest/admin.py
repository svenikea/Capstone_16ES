from django.contrib import admin
from .models import TaskList, Games

class gamelist(admin.ModelAdmin):
	list_display=('title', 'publisher', \
		'content', 'quanity', 'stock')

# Register your models here.
admin.site.register(Games, gamelist)
admin.site.register(TaskList)