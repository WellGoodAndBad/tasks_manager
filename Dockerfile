FROM python:3.8

COPY . /tasks_manager
WORKDIR /tasks_manager
RUN apt-get update && apt-get install -y netcat
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/tasks_manager/entrypoint.sh"]