FROM ubuntu:precise

RUN  apt-get update && apt-get install -y exim4-daemon-light
ADD  resources/update-exim4.conf.conf /etc/exim4/update-exim4.conf.conf
ADD  resources/exim4 /etc/init.d/exim4
ADD  resources/mailname /etc/mailname

CMD  /etc/init.d/exim4 start
