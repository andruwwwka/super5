FROM ubuntu:14.04

RUN apt-get update && \
	apt-get install -y libxml2-dev libxslt1-dev python3-dev python3-setuptools python3.4 build-essential python3-pip nginx libpq-dev mysql-client libmysqlclient-dev && \
	apt-get --assume-yes install -f libjpeg-dev zlib1g-dev && \
	ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib && \
	ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib && \
	ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

COPY requirements.txt /opt/app/requirements.txt

RUN sudo locale-gen "en_US.UTF-8"
ENV LC_CTYPE "en_US.UTF-8"
ENV LC_NUMERIC "en_US.UTF-8"
ENV LC_TIME "en_US.UTF-8"
ENV LC_COLLATE "en_US.UTF-8"
ENV LC_MONETARY "en_US.UTF-8"
ENV LC_MESSAGES "en_US.UTF-8"
ENV LC_PAPER "en_US.UTF-8"
ENV LC_NAME "en_US.UTF-8"
ENV LC_ADDRESS "en_US.UTF-8"
ENV LC_TELEPHONE "en_US.UTF-8"
ENV LC_MEASUREMENT "en_US.UTF-8"
ENV LC_IDENTIFICATION "en_US.UTF-8"
RUN locale
RUN pip3 install -r /opt/app/requirements.txt

COPY . /opt/app

VOLUME ["/opt/app/media"]

WORKDIR /opt/app

RUN openssl rand -base64 32 > secret_key.txt;

RUN python3 /opt/app/manage.py collectstatic --settings=super5.production_settings --noinput

RUN rm /etc/nginx/sites-enabled/default;
RUN ln -s /opt/app/Deploy/nginx.conf /etc/nginx/sites-enabled/;

EXPOSE 80