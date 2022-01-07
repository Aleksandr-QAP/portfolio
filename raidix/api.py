import requests
import json


class Hb:
    def __init__(self):
        self.base_url = "https://httpbin.org/"

    def get_api_headers(self):
        res = requests.get(self.base_url + 'headers')
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def test_get_api_codes(self, path):
        res = requests.get(self.base_url + '/status/' + path)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
