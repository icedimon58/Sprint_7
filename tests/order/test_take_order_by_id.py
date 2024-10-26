import allure
import requests
from data import HOST,ORDERS_URL


class TestTakeOrderByTrack:
    @allure.description('Код операции:200')
    @allure.title('Проверка получения заказа по номеру')
    def test_takin_order_by_track_positive(self,fill_payload_fields):
        payload = fill_payload_fields
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{HOST}{ORDERS_URL}', data=payload,headers=headers)
        track_id = response.json()['track']
        response = requests.get(f'{HOST}{ORDERS_URL}/track?t={track_id}')
        assert (response.status_code == 200
                and response.json()['order']['track'] == track_id)

    @allure.description('Код операции:400, ответ:"Недостаточно данных для поиска"')
    @allure.title('Проверка получения заказа без номера ')
    def test_takin_order_without_no_track_negative(self):
        response = requests.get(f'{HOST}{ORDERS_URL}/track')
        assert (response.status_code == 400 and
                response.json()['message'] == 'Недостаточно данных для поиска')

    @allure.description('Код операции:404, ответ:"Заказ не найден"')
    @allure.title('Проверка получения заказа с неправильным номером')
    def test_takin_order_with_wrong_track_negative(self):
        response = requests.get(f'{HOST}{ORDERS_URL}/track?t=11111111')
        assert (response.status_code == 404 and
                response.json()['message'] == 'Заказ не найден')