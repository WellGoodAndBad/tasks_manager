from .serializers import TaskSerialiser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
import django_filters.rest_framework


class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerialiser
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status', 'planned_completion_date']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return self.request.user.task_set.all()
        # else:
        #     status_tasks = self.request.query_params.get('status')
        #     planned_completion_date = self.request.query_params.get('planned_completion_date')
        #     tasks = Task.objects.filter(owner__id=self.request.user.id)
        #
        #     if status_tasks:
        #         return tasks.filter(status=status)
        #     elif planned_completion_date:
        #         return tasks.filter(planned_completion_date=planned_completion_date)
        #     elif status_tasks and planned_completion_date:
        #         return tasks.filter(status=status_tasks, planned_completion_date=planned_completion_date)
        #
        #     return tasks

