import allure
import requests
from data import HOST,COURIER_URL, generate_random_string


class TestCourierDelete:
    @allure.description('Код операции:200, курьер удален')
    @allure.title('Проверка успешного удаления курьера')
    def test_delete_courier_positive(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        requests.post(f'{HOST}/api/v1/courier', data=payload)
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        curier_id = response.json()['id']
        response = requests.delete(f'{HOST}{COURIER_URL}/{curier_id}')
        assert response.status_code == 200 and response.json()['ok'] is True

    @allure.description('Код операции:404, ответ: "Not Found."')
    @allure.title('Проверка  удаления курьера без указания ID')
    def test_delete_courier_no_id_negative(self):
        response = requests.delete(f'{HOST}{COURIER_URL}')
        assert (response.status_code == 404
                and response.json()['message'] == 'Not Found.')

    @allure.description('Код операции:404, ответ: "Курьера с таким id нет."')
    @allure.title('Проверка  удаления курьера c несуществующим ID')
    def test_delete_courier_no_id_negative(self):
        response = requests.delete(f'{HOST}{COURIER_URL}/-1')
        assert (response.status_code == 404
                and response.json()['message'] == 'Курьера с таким id нет.')
