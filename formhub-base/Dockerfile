FROM  larry/python
RUN   apt-get install -y libxml2-dev libxslt-dev default-jre git python-dev libjpeg-dev libfreetype6-dev zlib1g-dev libmysqlclient-dev
RUN   git clone https://github.com/modilabs/formhub.git
RUN   cd /formhub && git submodule init && git submodule update
RUN   pip install numpy --use-mirrors
# Symlinks for PIL/Pillow to find image libs
RUN   ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
RUN   ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
RUN   ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
RUN   easy_install -U distribute
RUN   pip install -r /formhub/requirements.pip && pip install -r /formhub/requirements-mysql.pip
