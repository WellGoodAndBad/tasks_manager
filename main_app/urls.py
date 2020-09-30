from django.urls import path

from . import views


urlpatterns = [
    path('tasks/', views.TaskViewSet.as_view({'get': 'list'})),
    path('create_task/', views.TaskViewSet.as_view({'post': 'create'})),
    # path('task/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve'})),
    path('task_update/<int:pk>/', views.TaskViewSet.as_view({'post': 'partial_update'})),
]