# Django settings for django_hello_world project.

import os

SECRET_KEY = 'your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = ['*']
LOOGADO_REDERECT_URL = 'console'
INSTALLED_APPS = [
    'django.contribt.admin',
    'project', # Your app 
db = {
    'DEFAULT': {
        'ENGINE': 'django.db.backends/sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'test': {
        'ENGINE': 'django.db.backends/sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3'),
    }
}
