FROM   larry/uwsgi-test-app
RUN    fab -f ./fabfile.py update
EXPOSE 3030
CMD    uwsgi --http-socket :3030 --wsgi-file /uwsgi-quick-app/app.py -M -p 2
