# password-checker
An password checker API using regex

Author: WaGjUb (Daniel Costa Valerio)

## Structure
We have two project directories: local\_running and aws\_running.
Both were written in python language. 
The idea was to create the password validation service in two different scenarios, thinking to run in a local server and to run in AWS as a serverless service.

### Local Running
This project runs on a local server using Flask.

#### Requiriments
- Python 3.8
- make

#### Quick run (all these command should to be runned in root directory (/password-checker/local\_running))
- Install dependences
	- make init
- run unit tests
	- make unit-test
- run integration tests
	- make integration-test
- run all tests
	- make test
- run API
	- make api -> it will start an api on localhost:8080 (can be modified in makefile)

#### Usage
you may use postman, curl or whatever you want to send a post request to endpoint "verifypassword"
e.g: curl --location --request POST 'http://localhost:8080/verifypassword' --header 'Content-Type: application/text' -d 'Daniel1@3'

#### Code Explanation

##### Verification
For validation of password I used a regex to match (or not) with the input string. It was used because it is native and the same in most of programming languages, it is easier to implement than create functions from zero and it is easy to mantain and create other flavors of match. (Basically the idea of regex is to be used in cases like that!)

##### API
The flask was used to build our API, it was choose becaus is very easy and fast to build an small API with flask and it have a good testing docs

##### Test
Pytest and Flask Testing was used to build our unit test and integration test
Our Unit test is testing the password regex matches, providing the inputs and checking the boolean output of password verifier
Our integration test is testing the integration between Flask api and password verifier code. This checks if server is up, if endpoint is returning and if the result os return matches with the password requirements

#### Project Structure
```
local\_running
├── Makefile (File that support to run and install dependences os project)
├── requirements.txt (project python dependences)
├── src (Dir with core code)
│   ├── \_\_init\_\_.py (with this you can try in python 3.3 < versions)
│   ├── password\_api.py (Code with flask api)
│   └── validate\_password.py (Code that verify the password)
└── tests (Dir with test code)
    ├── integration (Dir with integration test)
    │   ├── __init__.py
    │   └── test_api_password.py (Integration test of flask with password code)
    └── unit (Dir with unit test)
        ├── __init__.py
        └── test_password.py (Unitary test of password code)
```

### AWS Running
This project runs on AWS as serverless using API Gateway as API and AWS Lambda.

#### Requiriments
- You should to have SAM CLI installed to run this project locally or deploy this in your AWS
- Python 3.8
- make

#### Quick run (all these command should to be runned in root directory of project (/password-checker/aws\_running//password\_verify\_app))
- Install python dependences
	- make init
- run unit tests
	- make unit-test
- run integration tests (works only if deploy the code in you own AWS and change the stack variable on Makefile)
	- make integration-test
- run all tests
	- make test
- start an local API (an emulator of api gateway)
	- sam local start-api (default is http://localhost:3000/)
- To make the deploy on your AWS
	- sam deploy --guided

#### Usage
you may use postman, curl or whatever you want to send a post request to endpoint "verifypassword"

e.g: curl --location --request POST 'http://localhost:8080/verifypassword' --header 'Content-Type: application/text' -d 'Daniel1@3'

#### Code Explanation

##### Verification
For validation of password I used a regex to match (or not) with the input string. It was used because it is native and the same in most of programming languages, it is easier to implement than create functions from zero and it is easy to mantain and create other flavors of match. (Basically the idea of regex is to be used in cases like that!)

##### API
Here the API Gateway was used as our api

##### Test
Pytest Testing was used to build our unit test and integration test
Our Unit test is testing the password regex matches, providing the inputs and checking the boolean output of password verifier
Our integration test is testing the integration between API Gateway api and password verifier code. This checks if endpoint is returning and if the result os return matches with the password requirements (so If the apigateway and lambda are working together)

##### Project Structure
```
aws\_running
└── password\_verify\_app
    ├── Makefile
    ├── README.md (generated sam readme (it is util to understand what was generated))
    ├── \_\_init\_\_.py (with this you can try in python 3.3 < versions)
    ├── events (configure own events to run in local api (not using in this project))
    │   └── event.json (an dummy generated event (not using in this project))
    ├── samconfig.toml (pre configured file to deploy on AWS (generated when I did the deploy os application))
    ├── template.yaml (cloud formation template of app)
    ├── tests (Dir with test code)
    │   ├── __init__.py 
    │   ├── integration (Dir with integration test)
    │   │   ├── __init__.py
    │   │   └── test_api_gateway.py (Integration test of API Gateway with password code on lambda)
    │   ├── requirements.txt (test  python dependences)
    │   └── unit (Dir with unit test)
    │       ├── __init__.py
    │       ├── test_handler.py (Code with unit tests of password verifier with api gateway format request)
    │       └── test_password.py (Code with unit tests of password verifier)
    └── verify_password (Core code of lambda)
        ├── __init__.py
        ├── app.py (Code to process API gateway request and uses validate password to return (Lambda!))
        ├── requirements.txt (project python dependences)
        └── validate_password.py (Code that verify the password)
```
# EXTRA 
For your delight I deployed this app in an AWS endpoint, please tell me to request access ;D
