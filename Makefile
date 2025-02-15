
all: migrate run

migrate:
	@python3 django/manage.py makemigrations

kill:
	@sudo fuser -k 8000/tcp

run:
	@python3 django/manage.py runserver 8000