# Hackerspace website

Hackerspace website and hackerspace blog.


## Setup
### Prerequisites
- python3.8
- pipenv
    - install by `pip install pipenv`

1. Setup pipenv
    - `pipenv sync --dev`
2. Setup pre-commit hooks
    - `pipenv run precommmit`
3. Start webserver
    - `python manage.py runserver`
    - Note: make sure you migrate if you want to work with the database `python manage.py migrate`
