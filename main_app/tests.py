from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Task


class ApiTests(TestCase):

    username = 'Test_user'
    password = "Test_user_password"

    def test_create_task(self):
        client =  APIClient()
        user = User.objects.create_user(username=self.username, password=self.password)
        Task.objects.create(title="test_title",
                            description="test_description",
                            status="in_plan",
                            planned_completion_date="2000-01-01",
                            owner=user)
        resp = client.post('/auth/token/login/', {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(resp.status_code, 200)

    def test_get_tasks(self):
        client =  APIClient()
        user = User.objects.create_user(username=self.username, password=self.password)
        Task.objects.create(title="test_title",
                            description="test_description",
                            status="in_plan",
                            planned_completion_date="2000-01-01",
                            owner=user)
        resp = client.post('/auth/token/login/', {'username': self.username, 'password': self.password}, format='json')

        token = resp.data['auth_token']
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.get('/api/v1/tasks/')
        self.assertEqual(resp.status_code, 200)

    def test_change_task(self):
        client = APIClient()
        user = User.objects.create_user(username=self.username, password=self.password)
        Task.objects.create(title="test_title",
                            description="test_description",
                            status="in_plan",
                            planned_completion_date="2000-01-01",
                            owner=user)
        resp = client.post('/auth/token/login/', {'username': self.username, 'password': self.password}, format='json')

        token = resp.data['auth_token']
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        status = 'in_work'
        planned_completion_date = '2020-02-02'
        resp = client.post('/api/v1/task_update/1/', {'status': status,
                                                      'planned_completion_date': planned_completion_date}, format='json')

        self.assertEqual(resp.data['status'], status)
        self.assertEqual(resp.data['planned_completion_date'], planned_completion_date)
        self.assertEqual(len(resp.data['history_task']), 1)

