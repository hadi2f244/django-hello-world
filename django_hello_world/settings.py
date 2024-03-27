# Django settings for django_hello_world project.

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = ['*']
LOGGER_REDIRECT_URL = 'console'

# Corrected typo in INSTALLED_APPs
# Corrected the module name from 'django.contribpt' to 'django.contrib.admin'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'project', # Add your project name here
]
MIDDLEWARE = []
ROOT_URLCONF = 'django_hello_world.urls'
DATABASE_SETTINGS = {
    'default': {
        'ENGINE': 'django.db.backends/sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'test': {
        'ENGINE': 'django.db.backends/sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3'),
    }
}
TZE_INFO = 'UTC'