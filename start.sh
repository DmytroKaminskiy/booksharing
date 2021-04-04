#!/bin/bash

# ENV = ['dev', 'prod']
# if dev -> runserver, elif prod -> gunicorn run

if [[ "${MODE}" == "runserver" ]]; then
  ##
  python3 ./app/manage.py runserver 0:8000
  ##
elif [[ "${MODE}" == "worker" ]]; then
  CELERY_PID_FILE="/tmp/celery.pid"
  rm "${CELERY_PID_FILE}"

  celery \
    --app booksharing worker \
    --loglevel=INFO \
    --autoscale=0,20 \
    --pidfile="${CELERY_PID_FILE}"
fi
