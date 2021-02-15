import json
import re
#Running as main (AWS/local)
if __name__ == "app" :
    import validate_password
else:
    from verify_password import validate_password

def lambda_handler(event, context):
    password_checker = get_password_checker()
    print(event["body"])
    password_to_validate = event["body"]
    valid_ret = password_checker.is_valid_password(password_to_validate)
    return {
        "statusCode": 200,
        "body": json.dumps(valid_ret),
    }

def get_password_checker():
    return validate_password.password_checker()
