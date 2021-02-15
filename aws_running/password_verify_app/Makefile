stack-name=password-verify-app 
init:
	pip3 install -r verify_password/requirements.txt --user
	pip3 install -r tests/requirements.txt --user

test:
	AWS_SAM_STACK_NAME=$(stack-name) python3 -m pytest tests -v

unit-test: 
	python3 -m pytest tests/unit -v

integration-test: 
	AWS_SAM_STACK_NAME=$(stack-name) python3 -m pytest tests/integration -v


.PHONY: init test
