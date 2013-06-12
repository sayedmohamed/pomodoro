from django.shortcuts import render
from django.core import serializers

import models
from datetime import datetime


data = serializers.serialize('python', models.Task.objects.all())

def home(request):
	return render(request, 'index.html', dictionary={'view': 'home'})

def timer(request):
	return render(request, 'timer.html', dictionary={'view': 'timer'})

def tasks(request):
	return render(request, 'tasks.html', dictionary={'view': 'tasks', 'data': data})

def tasksNew(request):
	f = models.TaskForm(request.POST)
	# TODO: refactor
	if 'csrfmiddlewaretoken' and 'add' in request.POST:
		#f.completed = False
		#f.length = 25
		#f.created = datetime.now()
		f.save()
	
	return render(request, 'tasks_new.html', dictionary={'view': 'tasksNew', 'formset': f})

def history(request):
	return render(request, 'history.html', dictionary={'view': 'history'})
