FROM python:3.8-slim-buster
WORKDIR /src
RUN ["pip", "install", "pipenv"]
ADD Pipfile .
ADD Pipfile.lock .
RUN ["pipenv", "install", "--system", "--deploy"]
ADD . .
EXPOSE 8000

