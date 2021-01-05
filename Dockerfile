FROM python:3.8-slim-buster
WORKDIR /src
RUN ["pip", "install", "pipenv"]
ADD Pipfile .
ADD Pipfile.lock .
RUN ["pipenv", "install", "--system", "--deploy"]
ADD . .
ENTRYPOINT gunicorn --bind 0.0.0.0:$PORT hackerspace_site.wsgi:application
