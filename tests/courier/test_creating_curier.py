import allure
import requests
from data import HOST, generate_random_string,COURIER_URL


class TestCourierCreate:
    @allure.description('Код операции:201, курьер успешно создан')
    @allure.title('Проверка успешного создания курьера')
    def test_creating_courier_positive(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        response = requests.post(f'{HOST}{COURIER_URL}', data=payload)
        assert (response.status_code == 201
                and response.json()['ok'] is True)

    @allure.description('Код операции:409, ответ: "Этот логин уже используется. Попробуйте другой."')
    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_creating_two_same_couriers_negative(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        response = requests.post(f'{HOST}{COURIER_URL}', data=payload)
        assert (response.status_code == 409 and
                response.json()['message'] == "Этот логин уже используется. Попробуйте другой.")

    @allure.description('Код операции:400, ответ: "Недостаточно данных для создания учетной записи"')
    @allure.title('Проверка невозможности создания курьера без пароля')
    def test_creating_courier_without_password_negative(self):
        login = generate_random_string(10)
        payload = {
            "login": login
        }
        response = requests.post(f'{HOST}{COURIER_URL}', data=payload)
        assert (response.status_code == 400 and
                response.json()['message'] == "Недостаточно данных для создания учетной записи")

    @allure.description('Код операции:400, ответ: "Недостаточно данных для создания учетной записи"')
    @allure.title('Проверка невозможности создания курьера без логина')
    def test_creating_courier_without_login_negative(self):
        password = generate_random_string(10)
        payload = {
            "password": password
        }
        response = requests.post(f'{HOST}{COURIER_URL}', data=payload)
        assert (response.status_code == 400 and
                response.json()['message'] == "Недостаточно данных для создания учетной записи")

    @allure.description('Код операции:409, ответ: "Этот логин уже используется. Попробуйте другой."')
    @allure.title('Проверка невозможности создания курьеров с одинаковым именем')
    def test_creating_courier_with_existing_name_negative(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        last_pwd = payload['password']
        payload['password'] = '1234'
        response = requests.post(f'{HOST}{COURIER_URL}', data=payload)
        payload['password'] = last_pwd
        assert (response.status_code == 409 and
                response.json()['message'] == "Этот логин уже используется. Попробуйте другой.")
