from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.users_info, name='users_info'),
    path('login/', views.users_login, name='users_login'),
    path('register/', views.users_register, name='users_register'),
    path('logout/', views.users_logout, name='users_logout'),
]
