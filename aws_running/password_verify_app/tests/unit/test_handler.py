import json
import pytest

from verify_password import app

@pytest.fixture()
def apigw_event(request):
    return {
        "body": "{}".format(request.param),
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/verifypassword"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/verifypassword",
    }


def get_positive_cases():
    ret =  []
    ret.append("DanielV1@")
    ret.append("Sakureto4@")
    ret.append("AbTp9!fok")
    return ret

def get_negative_cases():
    ret =  []
    #empty value
    ret.append("")
    #less than 9 characters and repeated
    ret.append("aa")
    #less than 9 characters
    ret.append("ab")
    # missing digit and special character, repeated values
    ret.append("AAAbbbCc")
    # Repeated Characters
    ret.append("AbTp9!foo")
    #Repeated characters
    ret.append("AbTp9!foA")
    # space
    ret.append("AbTp9 fok")
    # less than 9 characters 
    ret.append("Ab1@")
    # integer
    ret.append(1)
    return ret

@pytest.mark.parametrize('apigw_event', get_positive_cases(), indirect=True)
def test_lambda_handler_positive_cases(apigw_event, mocker):
    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert True == data
    print(ret["body"])
    #assert data["message"] == "false"
    # assert "location" in data.dict_keys()

@pytest.mark.parametrize('apigw_event', get_negative_cases(), indirect=True)
def test_lambda_handler_false_cases(apigw_event, mocker):
    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert False == data
    print(ret["body"])
    #assert data["message"] == "false"
    # assert "location" in data.dict_keys()
