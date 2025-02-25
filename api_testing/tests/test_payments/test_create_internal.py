import json

import allure
import pytest
import requests

from api_testing.data import Urls, Payload


class TestCreateInternal:
    @pytest.mark.parametrize(
        'payload_type, endpoint, status_code',
        [
            (Payload.payload_internal_between_own_acc, Urls.CREATE_INTERNAL, 200),
            (Payload.payload_internal_between_own_acc, Urls.CREATE_INTERNAL_WITHOUT_VALIDATE_ONLY, 200),
            (Payload.payload_internal_differ_acc, Urls.CREATE_INTERNAL, 200),
            (Payload.payload_internal_differ_acc, Urls.CREATE_INTERNAL_WITHOUT_VALIDATE_ONLY, 200)
                    ]
    )
    @allure.title('Создание INTERNAL, happy pass')
    def test_create_internal_payment_positive_result(self, payload_type, endpoint, status_code):
        payload = payload_type
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{endpoint}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        #r1 = response.json()[part_1][param_1]
        #r2 = response.json()[part_2][param_2]
        assert status_code == response.status_code
        #assert r1 == value_1
        #assert r2 == value_2