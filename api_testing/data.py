

class Urls():
    URL = 'http://10.15.1.93:8080/BaaS/api/v1.0.0/party'
    CREATE_SEPA = '/paymentorder/penis-api/unl/sepa/pp/input?validate_only=true'
    CREATE_SWIFT = '/paymentorder/penis-api/unl/iso/swift/input?validate_only=true'
    CREATE_FPS = '/paymentorder/penis-api/unl/domestic/input/?validate_only=true'
    CREATE_TARGET = '/paymentorder/{id}/unl/tgt2/cus/input?validate_only=true'
    CREATE_INTERNAL = '/paymentorder/{id}/unl/generic/actrf/pp/input?validate_only=true'
    CREATE_EXCHANGE = '/forex/{id}/unl/create/spotdeal/api'
    CREATE_SEPA_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/sepa/pp/input'
    CREATE_SWIFT_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/iso/swift/input'
    CREATE_FPS_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/domestic/input/'
    CREATE_INTERNAL_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/generic/actrf/pp/input'

    CREATE_BENEFICIARY = 'https://dev-ibank.bocbs.cardpay-test.com/api/crud/beneficiary'


class Payload():
    payload_sepa = {
        "body": {
            "debitAccNumber": "GB81CARD04393909814209",
            "pmtCcy": "EUR",
            "pmtAmt": "1",
            "beneficiaryAccNumber": "LT950100100000123456",
            "beneficiaryName": "AMANDA",
            "beneficiaryCountryCode": "LT",
            "beneficiaryBankBic": "COBADEFF",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Via dei Coronari 178, 89"
            }],
            "chargeBearer": "SHA"
        }
    }

    payload_sepa_over_amount = {
        "body": {
            "debitAccNumber": "GB81CARD04393909814209",
            "pmtCcy": "EUR",
            "pmtAmt": "100000000",
            "beneficiaryAccNumber": "LT950100100000123456",
            "beneficiaryName": "AMANDA",
            "beneficiaryCountryCode": "LT",
            "beneficiaryBankBic": "COBADEFF",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Via dei Coronari 178, 89"
            }],
            "chargeBearer": "SHA"
        }
    }

    payload_swift_standard = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "pmtExecutionDate": "20241122",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_urgent = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "pmtExecutionDate": "20241122",
            "messagePriority": "URGENT",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_express = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "pmtExecutionDate": "20241122",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_with_intermediary_bank = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "pmtExecutionDate": "20241122",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021",
            "intermediary1Country": "NL",
            "intermediary1Bic": "BUNQNL2AXXX",
            "intermediary1Name": "BUNQ B.V.",
            "intermediary1Address": "AMSTERDAM NARITAWEG, 133"
        }
    }

    payload_swift_over_amount_standard = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1000000000",
            "pmtExecutionDate": "20241122",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_over_amount_urgent = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1000000000",
            "pmtExecutionDate": "20241122",
            "messagePriority": "URGENT",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_over_amount_express = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1000000000",
            "pmtExecutionDate": "20241122",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_over_amount_with_intermediary_bank = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "GBP",
            "pmtAmt": "1000000000",
            "pmtExecutionDate": "20241122",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021",
            "intermediary1Country": "NL",
            "intermediary1Bic": "BUNQNL2AXXX",
            "intermediary1Name": "BUNQ B.V.",
            "intermediary1Address": "AMSTERDAM NARITAWEG, 133"
        }
    }

    payload_swift_usd = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "USD",
            "pmtAmt": "1",
            "pmtExecutionDate": "20241122",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_eur = {
        "body": {
            "debitAccNumber": "GB38CARD04393901812968",
            "debitValueDate": "20241112",
            "pmtCcy": "EUR",
            "pmtAmt": "1",
            "pmtExecutionDate": "20241122",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "IT60X0542811101000000123456",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiaryBankBic": "BCITITMMXXX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_fps = {
        "body": {
            "debitAccNumber": "GB81CARD04393909814209",
            "debitValueDate": "20241008",
            "pmtCcy": "GBP",
            "pmtAmt": "0.3",
            "pmtExecutionDate": "20241022",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "48820508",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "ROME",
            "beneficiaryCountryCode": "IT",
            "beneficiarySortCode": "231470",
            "beneficiaryBankClearingSystemIdCode": "SC",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_exchange = {
        "body": {
            "cust": "87969650559",
            "acctopay": "GB37CARD04393909872910",
            "buyAmt": "2",
            "ccyBought": "EUR",
            "ccySold": "GBP",
            "treasuryRate": "0.8",
            "dealerComment": "BUY 2 EUR"
        }
    }

    payload_internal = {
        "body": {
            "debitAccNumber": "GB81CARD04393909814209",
            "pmtAmt": "1",
            "pmtCcy": "USD",
            "debitCcy": "USD",
            "debitValueDate": "20241014",
            "creditAcc": "GB38CARD04393901812968",
            "remittanceInformation": "123"
        }
    }

    payload_create_beneficiary = [
        {
            "iban": "44556677",
            "country": "United Kingdom of Great Britain and Northern Ireland",
            "address": "LONDON BAKER STREET",
            "bankCode": "BARCGB22XXX",
            "bankCountry": "UNITED KINGDOM",
            "bankAddress": "LONDON 1 CHURCHILL PLACE",
            "bankName": "BARCLAYS BANK PLC",
            "name": "FIRST ENGLISH BANK LIMITED",
            "additionalInfo": "{\"sortCode\":\"112233\"}",
            "companyCif": "9865778595",
            "accountGroup": "null",#null взят в кавычки
            "paymentType": "Intrabank",
            "currency": "EUR",
            "email": "tester-check2@gmail.com",
            "nickname": "tester-check"
        }
    ]
