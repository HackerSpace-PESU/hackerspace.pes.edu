FROM python:3.8-alpine
WORKDIR /src
RUN ["pip", "install", "pipenv"]
ADD Pipfile .
ADD Pipfile.lock .
RUN ["pipenv", "install", "--system", "--deploy"]
ADD . .
RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "migrate"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]

