from api import Hb
import logging
import http.client

http.client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

hb = Hb()


def test_get_api_headers():
    status, result = hb.get_api_headers()
    assert status == 200


def test_get_api_codes():
    code = '200'
    path = str(code)
    status, result = hb.test_get_api_codes(path)
    assert status == 200
