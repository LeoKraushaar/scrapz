

all: migrate run

migrate:
	@python3 django/manage.py makemigrations

run:
	@python3 django/manage.py runserver