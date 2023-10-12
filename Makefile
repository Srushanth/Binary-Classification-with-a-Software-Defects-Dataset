install:
	pip install -r requirements.txt

docker-build:
	docker build -t srubar/binary-classification-with-a-software-defects-dataset:latest .

docker-run:
	docker run -p 8501:8501 srubar/binary-classification-with-a-software-defects-dataset:latest

docker-push:
	docker push srubar/binary-classification-with-a-software-defects-dataset:latest

test:
	python -m pytest -vv test_app.py

format:
	black app.py

lint:
	pylint app.py

all: install format lint test
