# mysql
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'formhub_dev',
#        'USER': 'formhub_dev',
#        'PASSWORD': '',
#    }
#}

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

TOUCHFORMS_URL = 'http://localhost:9000/'

MONGO_DATABASE = {
    'HOST': '192.168.1.5',
    'PORT': 27017,
    'NAME': 'formhub',
    'USER': '',
    'PASSWORD': ''
}