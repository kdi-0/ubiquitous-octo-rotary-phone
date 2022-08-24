from client import FTXClient
from dotenv import dotenv_values
import pprint

if __name__ == "__main__":
    config = dotenv_values(".env")
    FTX = FTXClient(config['KEY'], config['SECRET'])
    r = FTX._request('GET', 'account')
    print(r.status_code)
    pp = pprint.PrettyPrinter()
    pp.pprint(r.json())
