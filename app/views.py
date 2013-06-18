from django.shortcuts import render
from django.http import HttpResponseRedirect

import models
from datetime import datetime


def home(request):
	return render(request, 'index.html', dictionary={'view': 'home'})

def timer(request):
	return render(request, 'timer.html', dictionary={'view': 'timer'})

def tasks(request):
	data = models.Task.objects.all()
	return render(request, 'tasks.html', dictionary={'view': 'tasks', 'data': data})

def tasksNew(request):
	if request.method == 'POST':
		f = models.TaskForm(request.POST)
		if f.is_valid():
			m = f.save(commit=False)
			m.actual = 0
			m.completed = False
			m.length = 25
			m.created = datetime.now()
			m.save()
			return HttpResponseRedirect('tasks/')
	else:
		f = models.TaskForm()
	
	return render(request, 'tasks_new.html', dictionary={'view': 'tasksNew', 'formset': f})

def history(request):
	return render(request, 'history.html', dictionary={'view': 'history'})
