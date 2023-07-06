test:
	poetry run django-admin test --pythonpath=. --settings=tests.settings

tox:
	poetry run tox

validate:
	poetry run pre-commit run --all-files
