from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/edit/<slug:pk>/', views.tasks_edit, name='tasks_edit'),
    path('tasks/delete/<slug:pk>/', views.tasks_delete, name='tasks_delete'),
]
