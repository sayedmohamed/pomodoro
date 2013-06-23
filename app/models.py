from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, AbstractBaseUser
from datetime import datetime


class Task(models.Model):
	name = models.CharField(max_length=100)
	user = models.CharField(max_length=100, editable=False)

	PRIORITIES = (
		('L', 'Low'),
		('M', 'Medium'),
		('H', 'High'),
	)
	priority = models.CharField(max_length=1, choices=PRIORITIES)

	# Date information for sorting
	created = models.DateField(editable=False)
	completed = models.BooleanField()
	done = models.DateField(editable=False)
	length = models.IntegerField(editable=False)

	# Amount of pomodoros
	estimate = models.IntegerField()
	actual = models.IntegerField()


class TaskForm(ModelForm):
	class Meta:
		model = Task
		exclude = ['actual', 'completed', 'done', 'user']
	
