#!/bin/bash

#execute init.db script
./init.db

#start gunicorn with config
exec gunicorn --config gunicorn_conf.py api:app
