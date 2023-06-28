install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 hexlet_code

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
