from api import PetFriends
from settings import valid_email, valid_passwords, invalid_email

pf = PetFriends()


def test_get_api_key_positive(email=valid_email, password=valid_passwords):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_negative_1(email=invalid_email, password=valid_passwords):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
