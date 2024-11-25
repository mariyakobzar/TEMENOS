import json

import allure
import pytest
import requests

from api_testing.data import Urls, Payload


class TestCreateSwift:
    @pytest.mark.parametrize(
        'payload_type, endpoint, status_code',
        [
            (Payload.payload_swift_standard, Urls.CREATE_SWIFT, 200),
            #(Payload.payload_swift_urgent, Urls.CREATE_SWIFT, 200),
            (Payload.payload_swift_express, Urls.CREATE_SWIFT, 200),
            (Payload.payload_swift_with_intermediary_bank, Urls.CREATE_SWIFT, 200),
            (Payload.payload_swift_usd, Urls.CREATE_SWIFT, 200),
            (Payload.payload_swift_eur, Urls.CREATE_SWIFT, 200),
            (Payload.payload_swift_standard, Urls.CREATE_SWIFT_WITHOUT_VALIDATE_ONLY, 200),
            (Payload.payload_swift_urgent, Urls.CREATE_SWIFT_WITHOUT_VALIDATE_ONLY, 200),
            (Payload.payload_swift_express, Urls.CREATE_SWIFT_WITHOUT_VALIDATE_ONLY, 200)
                    ]
    )
    @allure.title('Создание платежа SWIFT, happy pass')
    def test_create_swift_payment_positive_result(self, payload_type, endpoint, status_code):
        payload = payload_type
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{endpoint}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        assert status_code == response.status_code

    @pytest.mark.parametrize(
        'payload_type, status_code',
        [
            (Payload.payload_swift_over_amount_standard, 400),
            (Payload.payload_swift_over_amount_urgent, 400),
            (Payload.payload_swift_over_amount_express, 400),
            (Payload.payload_swift_over_amount_with_intermediary_bank, 400)

        ]
    )
    @allure.title('Создание платежа SWIFT, happy pass')
    def test_create_swift_payment_negative_result(self, payload_type, status_code):
        payload = payload_type
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{Urls.CREATE_SWIFT}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        # r1 = response.json()['body'][param_1]
        # r2 = response.json()['body'][param_2]
        assert status_code == response.status_code
        # assert r1 == value_1
        # assert r2 == value_2





