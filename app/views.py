from django.shortcuts import render

def home(request):
	return render(request, 'index.html', dictionary={'view': 'home'})

def timer(request):
	return render(request, 'timer.html', dictionary={'view': 'timer'})

def tasks(request):
	return render(request, 'tasks.html', dictionary={'view': 'tasks'})

def history(request):
	return render(request, 'history.html', dictionary={'view': 'history'})
