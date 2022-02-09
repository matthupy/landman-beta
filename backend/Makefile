.PHONY: create_super_user hard_reset init load_data nuke up

SETTINGS=backend.settings

SUPERUSER_USERNAME=default
SUPERUSER_EMAIL=default@example.com

#target create_super_user - Creates a default super user
create_super_user:
	python3 manage.py createsuperuser --settings=$(SETTINGS) --noinput --username $(SUPERUSER_USERNAME) --email $(SUPERUSER_EMAIL)

#target hard_reset - Nukes the environment and recreates it using defualt data
hard_reset:
	python3 manage.py reset_db --settings=$(SETTINGS) --noinput
	python3 manage.py migrate --settings=$(SETTINGS)
	python3 manage.py createsuperuser --settings=$(SETTINGS) --noinput --username $(SUPERUSER_USERNAME) --email $(SUPERUSER_EMAIL)
	python3 manage.py loaddata --settings=$(SETTINGS) fixtures/landman/*.json

#target init - Initialize environment. Only needs to be run once.
init:
	python3 manage.py makemigrations --settings=$(SETTINGS)
	python3 manage.py migrate --settings=$(SETTINGS)
	make create_super_user
	make load_data

#target load_data - Loads all data from stored fixtures
load_data:
	python3 manage.py loaddata --settings=$(SETTINGS) fixtures/landman/*.json

#target nuke - Nukes the environment without recreating anything
nuke:
	python3 manage.py reset_db --settings=$(SETTINGS) --noinput
	python3 manage.py clear_cache --settings=$(SETTINGS) --all

#target test - Runs all tests
test:
	python3 manage.py test --setting=$(SETTINGS) --noinput --failfast --debug-mode --buffer

#target up - Runs the environment
up:
	python3 manage.py runserver 0.0.0.0:8000