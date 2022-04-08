from api import PetFriends
from settings import valid_email, valid_passwords


def test_get_api_key_positive(email=valid_email, password=valid_passwords):
    status, result = PetFriends().get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_positive(filter=''):
    _, auth_key = PetFriends().get_api_key(valid_email, valid_passwords)
    status, result = PetFriends().get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

