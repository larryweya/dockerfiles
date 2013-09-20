FROM ubuntu:precise

# Hack for initctl not being available in Ubuntu
RUN  dpkg-divert --local --rename --add /sbin/initctl
RUN  ln -s /bin/true /sbin/initctl

RUN  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62 && echo 'deb http://nginx.org/packages/ubuntu/ precise nginx' | tee /etc/apt/sources.list.d/nginx.list
RUN  apt-get update && apt-get install -y nginx

ADD  resources/nginx.conf /etc/nginx/nginx.conf
RUN  rm /etc/nginx/conf.d/default.conf
ADD  resources/formhub.conf /etc/nginx/conf.d/formhub.conf

#EXPOSE 80:80
#CMD  /usr/sbin/nginx
