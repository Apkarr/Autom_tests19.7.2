import os

from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert isinstance(result, object)
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=""):
    _, auth_key = (valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='tuzik', animal_type='шпиц', age='1', pet_photo='images/tuzik.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "tuzik", "шпиц", "1", "images/tuzik.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 200
        assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='tuzik', animal_type='шпиц', age=1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

def test_get_api_key_not_correkt_email(valid_email = "235t7#$!@#3@yopmail.com", valid_password = "369" ):
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 403
    assert 'key'  not in result

def test_pet_with_negative_age(name='tuzik', animal_type='шпиц', age='-1', pet_photo='images/tuzik.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert age < '0'

def test_pet_with_name_from_symbols (name='&^#@!$%#@', animal_type='шпиц', age='1', pet_photo='images/tuzik.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == '&^#@!$%#@'

def test_pet_without_a_breed(name='tuzik', animal_type='', age='1', pet_photo='images/tuzik.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['animal_type'] == ''

def test_add_new_pet_with_invalid_name_move_1000_symbols(name='Gjlgjerrjggjsrpgjjgjljdflkjgsjdfgjeperggjldjgldffhlhjldf'
                                                              'nndfjgigjjghjghjefjfngnd,nvkdhhehojgoehgekjfghfvkfhdkdjh'
                                                              'gddghhekejrehgkhekrhgkehkghkfjhgdkfjhddkfffhkgeruhelwehf'
                                                              'ljhgljkdhgljkdhfgjdhfjhdfjhgdjhfkjdhfghdfgjhdlfkjghlejrh'
                                                              'trtheeurheekhekrhehoerojerljelrjlrgddngdnfgndfngeengkehkj'
                                                              'ukjshfkjqkhrhehhfkhfkhflkshglkghdkfjghkjfhfskjdhfksjddhfs'
                                                              'dhflshgljhglkjhrwkjehrkwjehrlqkjhrlkwjhtejkhtksjfskdhfksj'
                                                              'hdfksjyyuieuedlfhg;fhfgfhjdfhdfgnerghrghfjhskfhskghdldfjg'
                                                              'hdfjhddfkjhkfjhddfhjgd;fhg;dfjh;dfhdfhgkdfhfgjdfhgjkdfdhg'
                                                              'ddfhkddfhlddfhkdhfgkrhojo;jwperpwipeerig;jf;sfjsigpeeruii'
                                                              'rowpourwutwi84upuohfwhefkerhg98r9yu28yrhrwhhjfgsfrglhrwyu'
                                                              'r2y3t2rihtwhkwjkwehfk;shffksdbfksjbgkhgeytieytio3y4oiyri2'
                                                              '23yi2y324yyiu4yroiuwwruiwhefwhfkrkejht3o4yti4uyrwehfwljhw'
                                                              'jhkwehrklwhrkl2hriu2oiu2y3oi24i4yp3wheuwewhelrhwkhelhjksj'
                                                              'lflkhflksjshfwuehrioqugouyegwqouyegqwyuryjqrqwhf;sjdfshdj'
                                                              'sbsdmsbfv..dnfbdnf;wjf;hldhgqwdhjdgaadhasds/fjsdldkhshfl/'
                                                              'snfnrj’wlejfwejf’wjef’wjefjhwe;kjlkhefjwhegrjqgwehqwbbksb'
                                                              'df.sbndvsnsdbbdjhgeglhjwgqwerdfgtf', animal_type='шпиц',
                                                         age='1', pet_photo='images/tuzik.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result['name'] != name











