from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from . import functions


def tasks(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            tasks = models.Task.objects.filter(user=request.user)
            total = tasks.count()
        else:
            tasks = functions.get_tasks_cookies(request)
            total = len(tasks)

        context = {
            'tasks': tasks,
            'total': total,
        }

        return render(request, 'tasks/index.html', context)


def tasks_add(request):
    if request.method == 'GET':
        form = forms.TaskForm()

        context = {
            'form': form,
        }

        return render(request, 'tasks/add.html', context)
    elif request.method == 'POST':
        response = redirect('tasks')

        if request.user.is_authenticated:
            form = forms.TaskForm(request.POST)

            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.user = request.user
                new_task.save()
        else:
            title = request.POST.get('title')
            description = request.POST.get('description')
            tasks = functions.get_tasks_cookies(request)

            new_task = {
                'id': functions.set_task_id(tasks),
                'title': title,
                'description': description,
                'date': functions.get_datetime(),
            }

            tasks.append(new_task)

            response.set_cookie(
                'tasks',
                tasks,
                expires=functions.get_expire_datetime(),
            )

        return response


def tasks_edit(request, pk):
    if request.method == 'GET':
        context = {}

        if request.user.is_authenticated:
            task = get_object_or_404(models.Task, task_id=pk, user=request.user)
            form = forms.TaskForm(instance=task)
        else:
            tasks = functions.get_tasks_cookies(request)
            task = next(task for task in tasks if task.get('id') == pk)

            initial = {
                'title': task.get('title'),
                'description': task.get('description'),
            }

            form = forms.TaskForm(initial=initial)

            context.update(
                {'datetime': functions.str_to_datetime(task.get('date'))}
            )

        context.update({'task': task, 'form': form})

        return render(request, 'tasks/edit.html', context)
    elif request.method == 'POST':
        response = redirect('tasks')

        if request.user.is_authenticated:
            task = get_object_or_404(models.Task, task_id=pk, user=request.user)
            form = forms.TaskForm(request.POST, instance=task)

            if form.is_valid():
                form.save()
        else:
            tasks = functions.get_tasks_cookies(request)
            edit_task = next(task for task in tasks if task.get('id') == pk)

            title_updated = request.POST.get('title')
            description_updated = request.POST.get('description')

            edit_task.update(
                {'title': title_updated, 'description': description_updated}
            )

            updated_tasks = [
                edit_task if task.get('id') == pk else task for task in tasks
            ]

            response.set_cookie(
                'tasks',
                updated_tasks,
                expires=functions.get_expire_datetime(),
            )

        return response


def tasks_delete(request, pk):
    if request.method == 'GET':
        response = redirect('tasks')

        if request.user.is_authenticated:
            task = get_object_or_404(models.Task, task_id=pk, user=request.user)
            task.delete()
        else:
            tasks = functions.get_tasks_cookies(request)

            if len(tasks) == 1:
                response.delete_cookie('tasks')
            else:
                updated_tasks = [
                    task for task in tasks if task.get('id') != pk
                ]

                response.set_cookie(
                    'tasks',
                    updated_tasks,
                    expires=functions.get_expire_datetime(),
                )

        return response
