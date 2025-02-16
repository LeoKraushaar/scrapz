


freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

run:
	flask --app flask/app.py run