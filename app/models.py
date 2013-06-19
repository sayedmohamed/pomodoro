from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
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
	created = models.DateField(editable=False)
	completed = models.BooleanField()
	length = models.IntegerField(editable=False)

	# Amount of pomodoros
	estimate = models.IntegerField()
	actual = models.IntegerField()


class TaskForm(ModelForm):
	class Meta:
		model = Task
		exclude = ['actual', 'completed']
	

class Mortal(models.Model):
	user = models.OneToOneField(User)
	tasks = models.ManyToManyField(Task)

