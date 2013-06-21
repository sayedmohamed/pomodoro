from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import forms as auforms
from django.contrib import auth

import models
from datetime import datetime


def home(request):
	return render(request, 'index.html', dictionary={'view': 'home'})

def timer(request):
	return render(request, 'timer.html', dictionary={'view': 'timer'})

def tasks(request):
	data = models.Task.objects.all()
	if request.method == 'POST':
		value = request.POST['data']
		task = models.Task.objects.get(pk=value)
		task.completed = True
		task.done = datetime.now()
		task.save()
	return render(request, 'tasks.html', dictionary={'view': 'tasks', 'data': data, 'num': len(data)})

def tasksNew(request):
	if request.method == 'POST':
		f = models.TaskForm(request.POST)
		if f.is_valid():
			m = f.save(commit=False)
			m.actual = 0
			m.completed = False
			m.length = 25
			m.created = datetime.now()
			m.done = datetime.now()
			m.save()
			return HttpResponseRedirect('tasks/')
	else:
		f = models.TaskForm()
	
	return render(request, 'tasks_new.html', dictionary={'view': 'tasksNew', 'formset': f})

def history(request):
	data = models.Task.objects.all()
	return render(request, 'history.html', dictionary={'view': 'history', 'data': data})

def login(request):
	if request.user.is_authenticated():
		message = 'logged'
		auform = None
		if request.method == 'POST':
			auth.logout(request)
			message = ''
			auform = auforms.AuthenticationForm()
	elif request.method == 'POST':
		auform = auforms.AuthenticationForm(None, request.POST)
		message = ''
		if auform.is_valid():
			u = request.POST['username']
			p = request.POST['password']
			user = auth.authenticate(username=u, password=p)
			if user is not None:
				if user.is_active:
					auth.login(request, user)
					message = 'success'
	else:
		auform = auforms.AuthenticationForm()
		message = ''
	
	return render(request, 'login.html', dictionary={'view': 'login', 'auth': auform, 'msg': message})

