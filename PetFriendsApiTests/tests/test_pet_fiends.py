from api import PetFriends
from settings import valid_email, valid_passwords, invalid_email, invalid_passwords
import os


pf = PetFriends()


def test_get_api_key_positive(email=valid_email, password=valid_passwords):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_negative_1(email=invalid_email, password=valid_passwords):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_negative_2(email=valid_email, password=invalid_passwords):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_positive(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_negative(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_positive(name='Fat', animal_type='amorphous', age='2', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.add_information_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_negative(name='Мумий Тролль', animal_type='Владивосток', age='2000', pet_photo='images/cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.add_information_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_delete_self_pet_positive():
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet_from_database(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

def test_delete_self_pet_negative():
    _, auth_key = pf.get_api_key(valid_email, invalid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet_from_database(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

def test_update_self_pet_info_positive(name='Котэ', animal_type='хлебушек', age='33'):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len (my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

def test_update_self_pet_info_negative(name='Котэ', animal_type='хлебушек', age='очень много'):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len (my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_without_photo_positive(name='Гурмэ', animal_type='phonk', age='2'):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_photo_negative_1(name='Гурмэ', animal_type='phonk'):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_photo_negative_2(name='Гурмэ', age='2'):
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_photo_of_pet_positive(pet_photo='images/0.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert 'pet_photo' in result
    else:
        raise Exception("There is no my pets ")

def test_add_photo_of_pet_negative_1():
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert 'pet_photo' in result
    else:
        raise Exception("There is no my pets ")

def test_add_photo_of_pet_negative_2(pet_photo='images/dog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_passwords)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert 'pet_photo' in result
    else:
        raise Exception("There is no my pets ")