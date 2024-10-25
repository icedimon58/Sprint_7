import random
import string

HOST = 'https://qa-scooter.praktikum-services.ru'
COURIER_URL = '/api/v1/courier'
ORDERS_URL = '/api/v1/orders'

TEST_DATA_1 = {
    "firstName": "Дмитрий",
    "lastName": "Костылев",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 543 76 312 35",
    "rentTime": 8,
    "deliveryDate": "2025-07-06",
    "comment": "Прохождение теста API1",
    "color": ["GREY", "BLACK"]
}
TEST_DATA_2 = {
    "firstName": "Иван",
    "lastName": "Макаров",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 543 543 65 42",
    "rentTime": 5,
    "deliveryDate": "2024-52-06",
    "comment": "Прохождение теста API2",
    "color": ["BLACK"]
}
TEST_DATA_3 = {
    "firstName": "Василий",
    "lastName": "Костылев",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Прохождение теста API3",
    "color": ["BLACK"]
}
TEST_DATA_4 = {
    "firstName": "Олег",
    "lastName": "Иванов",
    "address": "Konoha, 142 apt.",
    "metroStation": 1,
    "phone": "+7 543 653 11 76",
    "rentTime": 1,
    "deliveryDate": "2024-12-12",
    "comment": "Прохождение теста API4",
    "color": []
}


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
