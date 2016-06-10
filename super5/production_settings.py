from super5.settings import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    '*'
]

with open('/opt/app/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/opt/app/django.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'),
#         'PORT': os.environ.get('POSTGRES_PORT_5432_TCP_PORT'),
#     }
# }

# \        'OPTIONS': {
#             'database': os.environ.get('MYSQL_ENV_MYSQL_DATABASE'),
#             'user': 'root',
#             'password': os.environ.get('MYSQL_ENV_MYSQL_ROOT_PASSWORD'),
#             'host': os.environ.get('MYSQL_PORT_3306_TCP_ADDR'),
#             'port': '',
#         },

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE_NAME'),
        'USER': 'root',
        'PASSWORD': os.environ.get('MYSQL_CHARSET_ENV_MYSQL_ROOT_PASSWORD'),
        'HOST': os.environ.get('MYSQL_CHARSET_PORT_3306_TCP_ADDR'),
        'PORT': '',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope'
    },
    'ACCESS_TOKEN_EXPIRE_SECONDS': 10,
}
