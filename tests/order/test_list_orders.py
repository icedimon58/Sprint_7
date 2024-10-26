import allure
import requests
from data import HOST, ORDERS_URL


class TestCreateOrders:

    @allure.description('Код операции:200, ответ: "limit = 4"')
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list_positive(self):
        response = requests.get(f'{HOST}{ORDERS_URL}?limit=4')
        assert (response.status_code == 200
                and response.json()['pageInfo']['limit'] == 4)