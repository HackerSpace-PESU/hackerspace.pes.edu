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
3. Setup development environment variables
    - Create a `.env` file.
    - Example for development:
    ```python
    DATABASE_URL = sqlite:///db.sqlite3
    DEBUG = True
    SUPERUSER_USERNAME = ...
    SUPERUSER_PASSWORD = ...
    ```
    - The DATABASE_URL can be set as required.
    - Example for production:

    ```python
    DATABASE_URL = ...
    DEBUG = False
    SECRET_KEY = ...
    ```
4. Start webserver
    - `pipenv run start`
    - Note: make sure you migrate if you want to work with the database `python manage.py migrate`
