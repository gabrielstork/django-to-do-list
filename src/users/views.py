from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import auth
from django.contrib import messages
from . import forms
from . import functions


def users_info(request):
    if request.method == 'GET':
        return render(request, 'users/info.html')


@user_passes_test(functions.check_is_visitor)
def users_login(request):
    if request.method == 'GET':
        form = forms.LoginForm()

        context = {
            'form': form,
        }

        return render(request, 'users/login.html', context)
    elif request.method == 'POST':
        user = functions.find_user(request, False)

        if user is not None:
            auth.login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('users_login')


@user_passes_test(functions.check_is_visitor)
def users_register(request):
    if request.method == 'GET':
        form = forms.RegisterForm()

        context = {
            'form': form,
        }

        return render(request, 'users/register.html', context)
    elif request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = functions.find_user(request, True)

            if user is not None:
                auth.login(request, user)
                return redirect('tasks')
            else:
                messages.error(request, 'Something went wrong.')
                return redirect('users_register')
        else:
            context = {
                'form': form,
            }

            return render(request, 'users/register.html', context)


@login_required
def users_logout(request):
    auth.logout(request)
    return redirect('tasks')
