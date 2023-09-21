from .base import *

import environ

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / '.env'))


SECRET_KEY = env.str('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PWD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env.str('db_name'),
#         'USER': env.str('db_user'),
#         'PASSWORD': env.str('db_password'),
#         'HOST': env.str('db_host'),
#         'PORT': env.str('db_port')
#     }
# }
