from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    return HttpResponse(Task.objects.all())


def edit(request, taskId):
    return HttpResponse("You're editing task %s." % taskId)
