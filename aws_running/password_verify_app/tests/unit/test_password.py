import pytest
from verify_password.validate_password import password_checker

@pytest.fixture
def password_checker_class():
    return password_checker()

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
    # invalid special character
    ret.append("AbTp9;fok")
    return ret


@pytest.mark.parametrize('test_input', get_positive_cases())
def test_positive_case(test_input, password_checker_class):
    response = password_checker_class.is_valid_password(test_input)
    assert response == True

@pytest.mark.parametrize('test_input', get_negative_cases())
def test_negative_case(test_input, password_checker_class):
    ret = password_checker_class.is_valid_password(test_input)
    assert ret == False
