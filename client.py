import time
import hmac
from requests import Request, Session


class FTXClient:
    URL = 'https://ftx.us/api/'

    def __init__(self, api_key=None, secret_key=None) -> None:
        # Session objects persist certain params + cookies accross requests
        # Improves performance
        self._session = Session()
        self.api_key = api_key
        self.secret_key = secret_key

    def _request(self, method: str, path: str, **kwargs):
        request = Request(method, self.URL+path, **kwargs)
        self._authenticate(request)
        response = self._session.send(request.prepare())
        return response

    def _authenticate(self, request: Request):
        ts = int(time.time() * 1000)
        prepared = request.prepare()
        signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode(
        )
        if prepared.body:
            signature_payload += prepared.body
        signature = hmac.new(self.secret_key.encode(),
                             signature_payload, 'sha256').hexdigest()
        request.headers[f'FTXUS-KEY'] = self.api_key
        request.headers[f'FTXUS-SIGN'] = signature
        request.headers[f'FTXUS-TS'] = str(ts)
