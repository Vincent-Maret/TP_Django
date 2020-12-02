'''Manage django views'''
from django.shortcuts import render, get_object_or_404
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


def finish_task(request, task_id):
    '''Set task.is_done to true'''
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))
