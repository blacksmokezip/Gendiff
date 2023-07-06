install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl