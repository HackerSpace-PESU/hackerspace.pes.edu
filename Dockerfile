FROM python:3.8-alpine
WORKDIR /src
ADD requirements.txt .
RUN ["pip", "install", "-r", "requirements.txt"]
ADD . .
RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "migrate"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]

