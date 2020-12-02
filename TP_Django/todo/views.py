'''Manage django views'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    '''Return a list of tasks'''
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return HttpResponse(render(request, 'todo/index.html', context))


def edit(request, task_id):
    '''Return a task edition page'''
    context = {'task_id': task_id}
    return HttpResponse(render(request, 'todo/edit.html', context))
