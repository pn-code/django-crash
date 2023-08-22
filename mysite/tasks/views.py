from django import forms
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task", min_length=1, max_length=100)

def index(request):
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add(request):
    return render(request, 'tasks/add.html', {'form': newTaskForm})