from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls')),
    path('users/', include('users.urls')),
]
