import os

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']
# mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['MYSQL_HOST'],
        'NAME': 'formhub',
        'USER': 'formhub',
        'PASSWORD': 'watermelon',
    }
}

# postgres
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'formhub_dev',
#        'USER': 'formhub_dev',
#        'PASSWORD': '',
#    }
#}

# sqlite
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'db.sqlite3',
#    }
#}

TOUCHFORMS_URL = 'http://localhost:9000/'

MONGO_DATABASE = {
    'HOST': os.environ['MONGO_HOST'],
    'PORT': 27017,
    'NAME': 'formhub',
    'USER': '',
    'PASSWORD': ''
}
BROKER_URL='amqp://guest:guest@{RABBITMQ_HOST}:5672'.format(RABBITMQ_HOST=os.environ['RABBITMQ_HOST'])
MEDIA_URL='/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['SMTP_HOST']
ADMINS = ()
SERVER_EMAIL = 'noreply@docker.ona.io'
DEFAULT_FROM_EMAIL = 'postmaster@docker.ona.io'
