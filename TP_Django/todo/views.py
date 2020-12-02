'''Manage django views'''
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Task


def index(request):
    '''Return a list of tasks'''
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'todo/index.html', context)


def edit(request, task_id):
    '''Return a task edition page'''
    context = {'task_id': task_id}
    return render(request, 'todo/edit.html', context)


def add_task(request):
    '''Add a task in database'''
    task_content = request.POST['newTask']
    new_task = Task(content=task_content, created_date=timezone.now())
    new_task.save()
    return HttpResponseRedirect(reverse('todo:index'))
