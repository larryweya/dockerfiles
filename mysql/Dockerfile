FROM    ubuntu:latest

# Hack for initctl not being available in Ubuntu
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl

RUN apt-get update
RUN apt-get install -y mysql-server

ADD resources/my.cnf /etc/mysql/my.cnf
