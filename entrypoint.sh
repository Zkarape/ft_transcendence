#!/bin/sh

python src/manage.py migrate --no-input
python src/manage.py collectstatic --no-input

gunicorn src.wsgi:application --bind 0.0.0.0:8000