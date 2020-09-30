from django.contrib import admin
from .models import Task, HistoryTask


admin.site.register(Task)
admin.site.register(HistoryTask)
