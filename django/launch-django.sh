#!/bin/bash

set -e

wait_for_postgres() {
    until nc -z postgres 5432; do
        echo "Waiting for postgres to be available..."
        sleep 5s
    done
    echo "Postgres is up and running."
}
prepare_django() {
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
    python manage.py createadminuser
}
launch_django() {
    gunicorn \
        --config core/gunicorn.py \
        core.wsgi:application
}
main() {
    wait_for_postgres
    echo "Preparing django..."
    prepare_django
    echo "Launching django..."
    launch_django
    echo "Django is running successfully."
}
main
