#!/bin/sh

# Для БД на хосте
#netstat -nr | grep '^0\.0\.0\.0' | awk '{print $2" host.docker.internal"}' >> /etc/hosts

# На случай если БД бдует долго запускаться
#while ! curl postgres:5432/ 2>&1 | grep '52'; do sleep 1; done

cd ./src

# Миграции и статика
python3 manage.py makemigrations
python3 manage.py migrate --noinput
python3 manage.py collectstatic --no-input --clear


# Запуск самого проекта
#gunicorn clients_portal.wsgi:application --chdir /restaurants_menu/src/ --bind 0.0.0.0:8000 --workers 2 --timeout 900 --error-logfile ../logs/gunicorn_web_error.log
python3 manage.py runserver 0.0.0.0:8027

exec "$@"