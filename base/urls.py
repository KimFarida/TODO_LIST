from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('update-task/<str:pk>/', TaskUpdate.as_view(), name='task-update'),
]