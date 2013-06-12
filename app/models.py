from django.db import models
from django import forms
from django.forms import ModelForm
from datetime import datetime

class Task(models.Model):
	name = models.CharField(max_length=100)

	PRIORITIES = (
		('L', 'Low'),
		('M', 'Medium'),
		('H', 'High'),
	)
	priority = models.CharField(max_length=1, choices=PRIORITIES)

	# Date information for sorting
	created = models.DateField()
	completed = models.BooleanField()
	length = models.IntegerField()

	# Amount of pomodoros
	estimate = models.IntegerField()
	actual = models.IntegerField()

class TaskForm(ModelForm):
	class Meta:
		model = Task

