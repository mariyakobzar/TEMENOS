import json

import allure
import pytest
import requests

from api_testing.data import Urls, Payload


class TestCreateSepa:
    @pytest.mark.parametrize(
        'payload_type, endpoint, status_code, param_1, value_1, param_2, value_2',
        [
            (Payload.payload_sepa, Urls.CREATE_SEPA, 200, 'pmtOrderProduct', 'SEPA', 'pmtCcy', 'EUR'),
            (Payload.payload_sepa, Urls.CREATE_SEPA_WITHOUT_VALIDATE_ONLY, 200, 'pmtOrderProduct', 'SEPA', 'pmtCcy', 'EUR')
                    ]
    )
    @allure.title('Создание платежа SEPA, happy pass')
    def test_create_sepa_payment_positive_result(self, payload_type, endpoint, status_code, param_1, value_1, param_2, value_2):
        payload = payload_type
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{endpoint}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        r1 = response.json()['body'][param_1]
        r2 = response.json()['body'][param_2]
        assert status_code == response.status_code
        assert r1 == value_1
        assert r2 == value_2


    @pytest.mark.parametrize(
        'payload_type, status_code, param_1, value_1, param_2, value_2',
        [
            (Payload.payload_sepa_over_amount, 400, 'status', 'failed', 'type', 'BUSINESS')
        ]
    )
    @allure.title('Создание платежа SEPA, негативные проверки')
    def test_create_sepa_payment_negative_result(self, payload_type, status_code, param_1, value_1, param_2, value_2):
        payload = payload_type
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{Urls.CREATE_SEPA}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        r1 = response.json()['header'][param_1]
        r2 = response.json()['error'][param_2]
        assert status_code == response.status_code
        assert r1 == value_1
        assert r2 == value_2




    #@allure.title('Создание платежа SEPA')
    #def test_create_sepa_payment_positive_result(self):
        #payload = Payload.payload_sepa
        #payload_string = json.dumps(payload)
        #response = requests.post(f'{Urls.URL}{Urls.CREATE_SEPA}', data=payload_string,
                                 #headers={'Content-Type': 'application/json'})
        #print(response.status_code)
        #print(response.text)
        #assert 200 == response.status_code