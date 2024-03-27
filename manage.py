# Django project manage.py file

import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_hello_world.settings')

if __name__ == '__main__':
    execute_from_command_line(sys.argv)