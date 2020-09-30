from django.db import models

# Create your models here.
class TaskList(models.Model):
	title = models.CharField(max_length=10)
	content = models.CharField(max_length=20)
	status = models.BooleanField(default=False)
	class Meta:
		db_table = 'List'
		#ordering = ['title', 'content', 'status']
		verbose_name = 'List'
		verbose_name_plural = 'Lists'
	def __str__(self):
		return self.title

class Games(models.Model):
	title = models.CharField(max_length=20)
	publisher = models.TextField()
	content = models.CharField(max_length=20)
	quanity = models.DecimalField(max_digits=100, \
	 decimal_places=0)
	stock = models.BooleanField(default=False)
	class Meta:
		db_table = 'Game List'
		#ordering = ['title', 'content', 'status']
		verbose_name = 'Game List'
		verbose_name_plural = 'Game Lists'
	def __str__(self):
		return self.title