import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = name
    return current_kit_body


def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token


def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == name


def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    assert response.status_code == 400


def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    assert response.status_code == 400


# Проверка №1
def test_create_kit_1_letter_in_kit_body_get_success_response():
    positive_assert('a')

 
# Проверка №2
def test_create_kit_511_letter_in_kit_body_get_success_response():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')


# Проверка №3
def test_create_kit_0_letter_in_kit_body_get_error_response():
    negative_assert_code_400('')


# Проверка №4
def test_create_kit_512_letter_in_kit_body_get_error_response():
    negative_assert_code_400('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')


# Проверка №5
def test_create_kit_eng_letter_in_kit_body_get_success_response():
    positive_assert('QWErty')


# Проверка №6
def test_create_kit_rus_letter_in_kit_body_get_success_response():
    positive_assert('Мария')


# Проверка №7
def test_create_kit_special_characters_in_kit_body_get_success_response():
        positive_assert('"№%@",')


# Проверка №8
def test_create_kit_space_allowed_in_kit_body_get_success_response():
    positive_assert(' Человек и КО ')


# Проверка №9
def test_create_kit_numbers_are_allowed_in_kit_body_get_success_response():
    positive_assert('123')


# Проверка №10
def test_create_kit_parameter_not_passed_in_kit_body_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_name(kit_body)


# Проверка №11
def test_create_kit_number_type_in_kit_body_get_error_response():
    kit_body = get_kit_body(123)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    
    assert response.status_code == 400