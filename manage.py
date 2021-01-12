#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django
from django.conf import settings
from django.contrib.auth import get_user_model


def create_super_user() -> None:
    """Create default super user for development mode."""
    django.setup()
    username = os.environ.get("SUPERUSER_USERNAME", "admin")
    password = os.environ.get("SUPERUSER_PASSWORD", "admin")

    user = get_user_model()

    if not user.objects.filter(username=username).exists():
        user = user.objects.create_superuser(username, "", password)
        print(f"Superuser with username {user.username} created.")
    else:
        print(f"Superuser with username {username} already exists.")


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackerspace_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if settings.DEBUG:
        create_super_user()
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
