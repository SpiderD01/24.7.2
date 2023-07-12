from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_add_new_pet_without_photo(name='Тимофей', animal_type='кот', age=1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_get_api_key_with_wrong_password_and_correct_mail(email=valid_email, password=invalid_password):
    status, result = pf.get_app_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_api_key_with_wrong_email_and_correct_password(email=invalid_email, password=valid_password):
    status, result = pf.get_app_key(email, password)
    assert status == 403
    assert 'key' not in result
