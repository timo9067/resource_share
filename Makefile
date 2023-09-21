dev-start:
	python manage.py runserver --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-migrate: 
	python manage.py migrate --settings=config.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) --settings=config.settings.dev

dev-shell: 
	python manage.py shell --settings=config.settings.dev

dev-rollback: 
	python manage.py migrate $(app) $(m) --settings=config.settings.dev

dev-test:
	python manage.py test -v 2 --settings=config.settings.dev