FROM ubuntu
# Hack for initctl not being available in Ubuntu
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl
RUN apt-get install -y wget
RUN wget -qO - http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -
RUN echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee /etc/apt/sources.list.d/rabbitmq.list
RUN apt-get update
RUN apt-get install -y rabbitmq-server
#EXPOSE 5672:5672
CMD /usr/sbin/rabbitmq-server
