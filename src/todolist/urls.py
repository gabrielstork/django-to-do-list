from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls')),
    path('user/', include('users.urls')),
]
