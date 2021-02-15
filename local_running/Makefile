port = 8080
host = localhost

init:
	pip3 install -r requirements.txt --user

test:
	python3 -m pytest tests -v

api:
	python3 src/password_api.py $(host) $(port)

unit-test:
	python3 -m pytest tests/unit -v

integration-test:
	python3 -m pytest tests/integration -v

.PHONY: init test
