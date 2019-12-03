# alias m='make'
HOST=0.0.0.0:8000

pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}
	@echo "Arquivos .pyc excluídos"

pycache:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} \;
	@echo "Arquivos __pycache__ excluídos"

build:
    rm --force --recursive build/
    rm --force --recursive dist/
    rm --force --recursive *.egg-info
	@echo "Arquivos de sistema excluídos"

comments:
	sed '/^[[:blank:]]*#/d;s/#.*//' **/*.py
	@echo "Comentários removidos"

migration:
	find . -type d -name 'migrations' -prune -exec rm -rf {} \;
	@echo "Migrações de banco excluídas"

clean-all:
	pyc
	build
	pycache
	comments
	migrations
	@echo "Remoção completa"

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
    flake8 --exclude=.tox

run:
	python manage.py runserver $(HOST)  # --settings=src.settings.dev

# make te APP=<app_name>
te:
	python manage.py migrate  # --database=<name>
	python manage.py --app $(APP)

# make tions APP=<app_name>
ti:
	python manage.py makemigrations
	python manage.py makemigrations --app $(APP)

usr:
	python manage.py createsuperuser

shell:
	python manage.py shell

collect:
	python manage.py collectstatic

truncate:
	python manage.py sqlflush

dump:
	python manage.py dumpdata --format=json --all --natural --indent=4 --database=default > db_dump.json

populate:
	python manage.py loaddata db_dump.json  # database=production
