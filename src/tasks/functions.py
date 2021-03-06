import ast
import datetime
import string
import random

CHARS = string.ascii_letters + string.digits


def generate_id():
    return ''.join(random.choices(CHARS, k=8))


def get_tasks_cookies(request):
    tasks_cookies = request.COOKIES.get('tasks')

    if tasks_cookies is not None:
        tasks = ast.literal_eval(tasks_cookies)
    else:
        tasks = []

    return tasks


def get_datetime():
    return str(datetime.datetime.now())


def str_to_datetime(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def get_expire_datetime():
    now = datetime.datetime.now()
    expire = now.replace(year=(now.year + 1))
    return expire
