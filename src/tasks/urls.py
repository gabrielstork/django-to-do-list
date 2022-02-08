from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('task/add/', views.tasks_add, name='tasks_add'),
    path('task/edit/<int:pk>/', views.tasks_edit, name='tasks_edit'),
    path('task/delete/<int:pk>/', views.tasks_delete, name='tasks_delete'),
]
