import allure
import requests

from data import HOST, COURIER_URL


class TestCourierLogin:
    @allure.description('Код операции:200, курьер успешно создан')
    @allure.title('Проверка успешного логина созданного курьера')
    def test_curier_login_success(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        assert (response.status_code == 200
                and response.json()['id'] is not None)

    @allure.description('Код операции:400, ответ: "Недостаточно данных для входа"')
    @allure.title('Проверка невозможности авторизации курьера без пароля')
    def test_curier_login_no_password_nagetive(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        last_pwd = payload['password']
        payload['password'] = ''
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        payload['password'] = last_pwd
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для входа')

    @allure.description('Код операции:400, ответ: "Недостаточно данных для входа"')
    @allure.title('Проверка невозможности авторизации курьера без логина')
    def test_curier_login_no_login_nagetive(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        last_pwd = payload['login']
        payload['login'] = ''
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        payload['login'] = last_pwd
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для входа')

    @allure.description('Код операции:404, ответ: "Учетная запись не найдена"')
    @allure.title('Проверка невозможности авторизации с неверным паролем')
    def test_curier_login_wrong_password_negative(self, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        last_pwd = payload['password']
        payload['password'] = '1234'
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        payload['password'] = last_pwd
        assert (response.status_code == 404
                and response.json()['message'] == 'Учетная запись не найдена')
