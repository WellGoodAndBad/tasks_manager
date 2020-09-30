
FROM python:3.8

COPY . /tasks_manager
WORKDIR /tasks_manager
RUN apt-get update -y
RUN pip install -r requirements.txt