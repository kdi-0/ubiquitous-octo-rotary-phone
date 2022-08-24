from client import FTXClient
from dotenv import dotenv_values

if __name__ == "__main__":
    config = dotenv_values(".env")
    FTX = FTXClient(config['KEY'], config['SECRET'])
    r = FTX._request('GET', 'markets')
    print(r)
