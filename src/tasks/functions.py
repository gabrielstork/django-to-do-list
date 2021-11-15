import ast
import datetime


def get_tasks_cookies(request):
    tasks_cookies = request.COOKIES.get('tasks')

    if tasks_cookies is not None:
        tasks = ast.literal_eval(tasks_cookies)
    else:
        tasks = []

    return tasks


def set_task_id(tasks):
    if len(tasks) == 0:
        return 1
    else:
        last_id = tasks[-1].get('id')
        return last_id + 1


def get_datetime():
    return str(datetime.datetime.now())


def str_to_datetime(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def get_expire_datetime():
    now = datetime.datetime.now()
    expire = now.replace(year=(now.year + 1))
    return expire
