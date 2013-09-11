FROM  larry/python
RUN   apt-get install -y libxml2-dev libxslt-dev default-jre git python-dev libjpeg-dev libfreetype6-dev zlib1g-dev
RUN   git clone https://github.com/modilabs/formhub.git
ADD   resources/fabfile.py /fabfile.py 
ADD   resources/local_settings.py /formhub/formhub/local_settings.py
