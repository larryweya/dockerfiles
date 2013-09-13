FROM    larry/formhub
ADD     resources/fabfile.py /fabfile.py 
ADD     resources/local_settings.py /formhub/formhub/local_settings.py
ADD     resources/wsgi.py /formhub/wsgi.py
ADD     resources/wsgi.ini /formhub/wsgi.ini
RUN     fab -f ./fabfile.py update:branch=master
WORKDIR /formhub
ENV     DJANGO_SETTINGS_MODULE formhub.settings
CMD     python manage.py syncdb --noinput && python manage.py migrate && python manage.py collectstatic --noinput && /usr/local/bin/uwsgi --ini wsgi.ini
