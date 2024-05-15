build:
	docker compose build --no-cache
	
up:
	docker compose up -d

migrate:
	docker compose run app python manage.py migrate

makemigrations:
	docker compose run app python manage.py makemigrations

stop:
	docker compose stop

test:
	docker compose run app pytest

statics:
	docker compose run app python manage.py collectstatic

createsuperuser:
	docker compose run app python manage.py createsuperuser

bash:
	docker compose run app bash

lint:
	docker compose run app ruff check .

format:
	docker compose run app ruff format .
