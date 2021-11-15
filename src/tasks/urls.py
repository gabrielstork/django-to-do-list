from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/add/', views.add, name='add'),
    path('task/edit/<int:pk>/', views.edit, name='edit'),
    path('task/delete/<int:pk>/', views.delete, name='delete'),
]
