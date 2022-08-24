from email import header
import time
import hmac
from collections import defaultdict
import requests
# config = {"USER": "foo", "EMAIL": "foo@example.org"}


class FTXClient:
    URL = 'https://ftx.us/api'

    def __init__(self, api_key=None, secret_key=None) -> None:
        self.api_key = api_key
        self.secret_key = None

    def get(self, endpoint)


ts = int(time.time() * 1000)
base_url = "https://ftx.us/api/account"
request = Request('GET', base_url)
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new(config['SECRET'].encode(),
                     signature_payload, 'sha256').hexdigest()
prepared.headers[f'FTXUS-KEY'] = config['KEY']
prepared.headers[f'FTXUS-SIGN'] = signature
prepared.headers[f'FTXUS-TS'] = str(ts)
r = requests.get(base_url, headers=prepared)
r.status_code
