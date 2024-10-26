import json
import allure
import pytest
import requests
from data import HOST, ORDERS_URL, TEST_DATA_1, TEST_DATA_2, TEST_DATA_3, TEST_DATA_4


class TestCreateOrders:
    @pytest.mark.parametrize('color', [[TEST_DATA_1], [TEST_DATA_2], [TEST_DATA_3], [TEST_DATA_4]])
    @allure.description('Код операции:201, в ответе присутствует поле "track"')
    @allure.title('Проверка создания заказа с разным значением поля "Color"')
    def test_order_creating_positive(self, color):
        payload = color
        payload = json.dumps(payload)
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{HOST}{ORDERS_URL}', data=payload, headers=headers)
        assert (response.status_code == 201
                and response.json()['track'])
