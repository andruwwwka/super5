#!/usr/bin/env bash

sudo /etc/init.d/nginx start;
uwsgi --socket /tmp/uwsgi.sock --module super5.wsgi --chmod-socket=777 --processes=10