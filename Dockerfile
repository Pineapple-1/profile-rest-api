FROM python:3.9-alpine


ENV PYTHONUNBUFFER 1

WORKDIR /profile-rest-api

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:80

