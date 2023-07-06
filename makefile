test:
	poetry run django-admin test --pythonpath=. --settings=tests.settings

validate:
	poetry run pre-commit run --all-files
