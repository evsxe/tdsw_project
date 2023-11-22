#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

from sql_scripts.load_data import create_tables, alter_slave


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tdsw_service.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    create_tables()
    alter_slave()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
