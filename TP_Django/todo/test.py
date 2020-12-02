from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


def create_task(task_text):
    '''Create a task with given text'''
    return Task.objects.create(content=task_text)


class TaskTests(TestCase):
    def test_task_creation(self):
        '''Chould create task test'''
        c = Client()
        c.post(reverse('todo:addTask'), {'newTask': 'test'})
        response = c.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context['task_list'], ['<Task: test>'])

    def test_empty_task(self):
        '''If empty text, task shoudn't be create'''
        c = Client()
        c.post(reverse('todo:addTask'), {'newTask': ''})
        response = c.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context['task_list'], [])

    def test_empty_task_update(self):
        '''If empty text, task shoudn't be create'''
        c = Client()
        c.post(reverse('todo:addTask'), {'newTask': 'test'})
        c.post(reverse('todo:updateTask', kwargs={
               'task_id': 1}), {'updatedTask': ''})
        response = c.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context['task_list'], ['<Task: test>'])
