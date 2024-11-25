import json

import allure
import pytest
import requests

from api_testing.data import Urls, Payload


class TestCreateBeneficiary:
    @allure.title('Создание бенефициара, happy pass')
    def test_create_beneficiary_payment_positive_result(self):
        payload = Payload.payload_create_beneficiary
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{Urls.CREATE_BENEFICIARY}', data=payload_string,
                                 headers={'Content-Type': 'application/json'})
        assert response.status_code == 200