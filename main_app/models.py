from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TasksBaseModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    planned_completion_date = models.DateField(blank=True)


class Task(TasksBaseModel):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_plan', 'Запланированная'),
        ('in_work', 'В Работе'),
        ('done', 'Завершенна'),
    )
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class HistoryTask(TasksBaseModel):
    status = models.CharField(max_length=250)
    history_task = models.ForeignKey(Task, on_delete=models.CASCADE)