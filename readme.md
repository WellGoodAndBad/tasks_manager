## rest-api tasks managers
- docker-compose build
- docker-compose up

##### регистрация по адресу: -  /auth/users/

пример запроса для регистрации:
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'username=<user_name>&password=<user_password>' 'http://127.0.0.1:8000/auth/users/'

##### для получения токена: - /auth/token/login/

пример запроса:
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'username=<user_name>&password=<user_password>' 'http://127.0.0.1:8000/auth/token/login/'

##### для создания задачи(task): - /api/v1/create_task/

пример запроса:
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Token <TOKEN>"  -d 'title=<title>&description=<description_task>&status=<status>&planned_completion_date=<planned_date>' 'http://127.0.0.1:8000/api/v1/create_task/'

##### для запроса всех задач: - /api/v1/tasks/

возможные параметры: -  status(/api/v1/tasks/?status=<status>), 
planned_completion_date (/api/v1/tasks/?planned_completion_date=<planned_date>), 
или оба вместе (/api/v1/tasks/?status=<status>&planned_completion_date=<1999-12-13>),

пример запроса:
curl -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Token <TOKEN>" 'http://127.0.0.1:8000/api/v1/tasks/'

##### для изменения задачи: - /api/v1/task_update/<id_task>/

пример запроса:
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" 
-H "Authorization: Token <TOKEN>" -d 'title=<title>&description=<description_task>&status=<status>&planned_completion_date=<1999-12-29>' 'http://127.0.0.1:8000/api/v1/task_update/<id_task>/'
