SHELL := /bin/bash

manage_py := docker exec -it backend python3 app/manage.py

runserver:
	$(manage_py) runserver 0:8000

collectstatic:
	$(manage_py) collectstatic --noinput && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static web:/etc/nginx/static

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

build-dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

build: build-dev collectstatic
