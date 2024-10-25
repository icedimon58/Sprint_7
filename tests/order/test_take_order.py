import allure
import requests
from data import HOST,COURIER_URL,ORDERS_URL


class TestTakeOrders:
    @allure.description('Код операции:200, заказ успешно принят.')
    @allure.title('Проверка принятия заказа курьером')
    def test_takin_order_positive(self, register_new_courier_and_return_login_password, fill_payload_fields):
        payload = fill_payload_fields
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{HOST}{ORDERS_URL}', data=payload, headers=headers)
        track_id = response.json()['track']
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        courier_id = response.json()['id']
        response = requests.put(f'{HOST}{ORDERS_URL}/accept/{track_id}?courierId={courier_id}')
        assert (response.status_code == 200
                and response.json()['ok'] is True)

    @allure.description('Код операции:400, ответ:"Недостаточно данных для поиска"')
    @allure.title('Проверка принятия заказа курьером без указания номера курьера')
    def test_takin_order_no_curier_id_negative(self, register_new_courier_and_return_login_password,
                                               fill_payload_fields):
        payload = fill_payload_fields
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{HOST}{ORDERS_URL}', data=payload, headers=headers)
        track_id = response.json()['track']
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        response = requests.put(f'{HOST}{ORDERS_URL}/accept/{track_id}?courierId=')
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для поиска')

    @allure.description('Код операции:404, ответ:"Курьера с таким id не существует"')
    @allure.title('Проверка принятия заказа курьером с неверным номером курьера')
    def test_takin_order_wrong_curier_id_negative(self, register_new_courier_and_return_login_password,
                                                  fill_payload_fields):
        payload = fill_payload_fields
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{HOST}{ORDERS_URL}', data=payload, headers=headers)
        track_id = response.json()['track']
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        response = requests.put(f'{HOST}{ORDERS_URL}/accept/{track_id}?courierId=-1')
        assert (response.status_code == 404
                and response.json()['message'] == 'Курьера с таким id не существует')

    @allure.description('Код операции:400, ответ:"Недостаточно данных для поиска"')
    @allure.title('Проверка принятия заказа курьером с отсутствующим номером заказа')
    def test_takin_order_no_track_id_negative(self, register_new_courier_and_return_login_password,
                                              fill_payload_fields):
        payload = fill_payload_fields
        headers = {"Content-type": "application/json"}
        requests.post(f'{HOST}{ORDERS_URL}', data=payload, headers=headers)
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        courier_id = response.json()['id']
        response = requests.put(f'{HOST}{ORDERS_URL}/accept/courierId={courier_id}')
        assert (response.status_code == 400
                and response.json()['message'] == 'Недостаточно данных для поиска')

    @allure.description('Код операции:404, ответ:"Заказа с таким id не существует"')
    @allure.title('Проверка принятия заказа курьером с неверным номером заказа')
    def test_takin_order_wrong_track_id_negative(self, register_new_courier_and_return_login_password,
                                                 fill_payload_fields):
        payload = fill_payload_fields
        headers = {"Content-type": "application/json"}
        requests.post(f'{HOST}{ORDERS_URL}', data=payload, headers=headers)
        payload = register_new_courier_and_return_login_password
        requests.post(f'{HOST}{COURIER_URL}', data=payload)
        response = requests.post(f'{HOST}{COURIER_URL}/login', data=payload)
        courier_id = response.json()['id']
        response = requests.put(f'{HOST}{ORDERS_URL}/accept/-1?courierId={courier_id}')
        assert (response.status_code == 404
                and response.json()['message'] == 'Заказа с таким id не существует')
