

class Urls():
    URL = 'http://10.15.1.93:8080/BaaS/api/v1.0.0/party'
    CREATE_SEPA = '/paymentorder/penis-api/unl/sepa/pp/input?validate_only=true'
    CREATE_SWIFT = '/paymentorder/penis-api/unl/iso/swift/input?validate_only=true'
    CREATE_FPS = '/paymentorder/penis-api/unl/unlgbp/input/?validate_only=true'
    CREATE_CHAPS = '/paymentorder/penis-api/unl/unlcps/input/?validate_only=true'
    CREATE_TARGET = '/paymentorder/{id}/unl/tgt2/cus/input?validate_only=true'
    CREATE_INTERNAL = '/paymentorder/penis-api/unl/generic/actrf/pp/input?validate_only=true'
    CREATE_EXCHANGE = '/forex/{id}/unl/create/spotdeal/api'
    CREATE_SEPA_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/sepa/pp/input'
    CREATE_SWIFT_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/iso/swift/input'
    CREATE_FPS_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/unlgbp/input/'
    CREATE_CHAPS_WITHOUT_VALIDATE_ONLY = '/paymentorder/penis-api/unl/unlcps/input/'
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
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_urgent = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "messagePriority": "URGENT",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_express = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_with_intermediary_bank = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "1",
            "messagePriority": "URGENT",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
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
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "10000000000",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_over_amount_urgent = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "10000000000",
            "messagePriority": "URGENT",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_over_amount_express = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "10000000000",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_over_amount_with_intermediary_bank = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "GBP",
            "pmtAmt": "10000000000",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
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
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "USD",
            "pmtAmt": "1",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_swift_eur = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "debitValueDate": "20250226",
            "pmtCcy": "EUR",
            "pmtAmt": "1",
            "messagePriority": "EXPRESS",
            "beneficiaryAccNumber": "AL35202111090000000001234567",
            "beneficiaryName": "LUCIA LUI",
            "beneficiaryTownName": "TIRANA",
            "beneficiaryCountryCode": "AL",
            "beneficiaryBankBic": "SGSBALTX",
            "beneficiaryAddressLines": [{
                "beneficiaryAddressLine": "Flower street 8"
            }],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_fps = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "pmtCcy": "GBP",
            "pmtAmt": "2.5",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "48820508",
            "beneficiaryName": "FERNANDO ALONSO",
            "beneficiarySortCode":"231470",
            "beneficiaryBankClearingSystemIdCode": "SC",
            "beneficiaryAddressLines": [
                {
                    "beneficiaryAddressLine": "Flower street 8"
                }
            ],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_chaps = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "pmtCcy": "GBP",
            "pmtAmt": "1000000",
            "messagePriority": "STANDARD",
            "beneficiaryAccNumber": "48820508",
            "beneficiaryName": "FERNANDO ALONSO",
            "beneficiarySortCode": "231470",
            "beneficiaryBankClearingSystemIdCode": "SC",
            "beneficiaryAddressLines": [
                {
                    "beneficiaryAddressLine": "Flower street 8"
                }
            ],
            "chargeBearer": "SHA",
            "remittanceInformation": "Payment per Inv. 34452 dd. 31/01/21 Advertising revenue for January 2021"
        }
    }

    payload_exchange = {
        "body": {
            "cust": "100044",
            "acctopay": "GB72CARD04393972168978",
            "buyAmt": "2",
            "ccyBought": "EUR",
            "ccySold": "GBP",
            "treasuryRate":"0.8",
            "dealerComment":"BUY 2 EUR"
        }
    }

    payload_internal_between_own_acc = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "pmtAmt": "1",
            "pmtCcy": "EUR",
            "debitCcy": "EUR",
            "debitValueDate": "20250226",
            "creditAcc": "GB57CARD04393969894986",
            "remittanceInformation": "123"
        }
    }

    payload_internal_differ_acc = {
        "body": {
            "debitAccNumber": "GB26CARD04393916749147",
            "pmtAmt": "1",
            "pmtCcy": "EUR",
            "debitCcy": "EUR",
            "debitValueDate": "20250226",
            "creditAcc": "GB29CARD04393946865556",
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
