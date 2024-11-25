import json

import allure
import pytest
import requests

from api_testing.data import Urls, Payload


class TestCreateExchange:
    @pytest.mark.parametrize(
        'payload_type, endpoint, status_code',
        [
            (Payload.payload_exchange, Urls.CREATE_EXCHANGE, 200)
                    ]
    )
    @allure.title('Создание EXCHANGE, happy pass')
    def test_create_exchange_payment_positive_result(self, payload_type, endpoint, status_code):
        payload = payload_type
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{endpoint}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        #r1 = response.json()[part_1][param_1]
        #r2 = response.json()[part_2][param_2]
        assert status_code == response.status_code
        #assert r1 == value_1
        #assert r2 == value_2