from django.contrib import auth


def find_user(request, from_register_view):
    username = request.POST.get('username')

    if from_register_view:
        password = request.POST.get('password2')
    else:
        password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    return user


def check_is_visitor(user):
    return not user.is_authenticated
