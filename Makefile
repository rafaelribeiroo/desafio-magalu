# alias m='make'
HOST=0.0.0.0:8000

pyc:
	find . -name "*.pyc" -exec rm -f {} \;
	@echo "Arquivos .pyc excluídos"

pycache:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} \;
	@echo "Arquivos __pycache__ excluídos"

comments:
	sed '/^[[:blank:]]*#/d;s/#.*//' **/*.py
	@echo "Comentários removidos"

migration:
	rm -rf api/migrations
	@echo "Migrações de banco excluídas"

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

run:
	python manage.py runserver $(HOST)

# make ti APP=<app_name>
ti:
	python manage.py makemigrations
	python manage.py makemigrations api

te:
	python manage.py migrate

usr:
	python manage.py createsuperuser

sh:
	python manage.py shell

clt:
	python manage.py collectstatic

tr:
	python manage.py sqlflush

dp:
	python manage.py dumpdata -a -e=auth -e=contenttypes --format=json --indent=4 > data.json

populate:
	python manage.py loaddata products.json  # database=production
