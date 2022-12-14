import time
import hmac
from typing import Optional, Dict, Any
from requests import Request, Session
from websocket import WebSocketApp


class FTXClientHTTP:
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

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None):
        return self._request('GET', path, params=params)

    def _orderbook(self, market_name: str = 'BTC/USD', depth: int = 20):
        return self._get(f"markets/{market_name}/orderbook", {"depth": depth})

    def _submit_order(self, side: str, qty: str, type: str, market: str):
        pass


class RocketSocket:
    pass


class FTXClientWS:
    URI: str = 'wss://ftx.us/ws/'

    def __init__(self) -> None:
        pass

        pass

    def _connect(self,):
        pass

    def _subscribe(self):
        pass
