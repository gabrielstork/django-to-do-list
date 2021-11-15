from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import auth
from django.contrib import messages
from . import forms
from . import functions


@user_passes_test(functions.check_is_visitor)
def login(request):
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
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')


@user_passes_test(functions.check_is_visitor)
def register(request):
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
                return redirect('index')
            else:
                messages.error(request, 'Something went wrong.')
                return redirect('register')
        else:
            context = {
                'form': form,
            }

            return render(request, 'users/register.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')


def info(request):
    if request.method == 'GET':
        return render(request, 'users/info.html')
