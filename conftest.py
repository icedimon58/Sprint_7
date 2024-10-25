import json
import requests
import pytest
from data import HOST, generate_random_string, TEST_DATA_1, COURIER_URL


@pytest.fixture
def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    yield payload
    response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
    corier_id = response.json()['id']
    requests.delete(f'{HOST}{COURIER_URL}/{corier_id}')


@pytest.fixture
def fill_payload_fields():
    return json.dumps(TEST_DATA_1)
