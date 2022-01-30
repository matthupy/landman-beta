.PHONY: hard_reset load_data nuke

SETTINGS=backend.settings

SUPERUSER_USERNAME=admin
SUPERUSER_EMAIL=admin@example.com

#target hard_reset - Nukes the environment and recreates it using defualt data
hard_reset:
	python3 manage.py reset_db --settings=$(SETTINGS) --noinput
	python3 manage.py migrate --settings=$(SETTINGS)
	python3 manage.py createsuperuser --settings=$(SETTINGS) --noinput --username $(SUPERUSER_USERNAME) --email $(SUPERUSER_EMAIL)
	python3 manage.py loaddata --settings=$(SETTINGS) fixtures/landman/*.json

#target load_data - Loads all data from stored fixtures
load_data:
	python3 manage.py loaddata --settings=$(SETTINGS) fixtures/landman/*.json

#target nuke - Nukes the environment without recreating anything
nuke:
	python3 manage.py reset_db --settings=$(SETTINGS) --noinput

#target test - Runs all tests
test:
	python3 manage.py test --setting=$(SETTINGS) --noinput --failfast --debug-mode --buffer