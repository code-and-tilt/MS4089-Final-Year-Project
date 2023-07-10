install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black src/*.py

lint:
	pylint --disable=R,C src/*/*.py

test:
	python -m pytest -vv --cov=src/*/*.py

all:
	install lint black test