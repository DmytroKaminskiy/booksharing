SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver 0:8000

run_celery:
	celery -A booksharing worker -l info

migrate:
	$(manage_py) migrate

shell_plus:
	$(manage_py) shell_plus --print-sql

makemigrations:
	$(manage_py) makemigrations

pytest:
	pytest app/ --cov=app --cov-report html

flake8:
	flake8 app/

build:
	docker-compose up -d
