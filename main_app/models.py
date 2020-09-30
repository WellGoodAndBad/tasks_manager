from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_plan', 'Запланированная'),
        ('in_work', 'В Работе'),
        ('done', 'Завершенна'),
    )

    title = models.CharField(max_length=250)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250, choices=STATUS_CHOICES)
    planned_completion_date = models.DateField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class HistoryTask(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=250)
    planned_completion_date = models.DateField(blank=True)
    history_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='children')