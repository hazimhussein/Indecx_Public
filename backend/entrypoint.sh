#!/bin/shd

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn project.wsgi:application --bind 0.0.0.0:8000 --timeout 7200