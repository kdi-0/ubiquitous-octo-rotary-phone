from client import FTXClientHTTP, FTXClientWS
from dotenv import dotenv_values
import pprint
import asyncio
import websocket


def on_message(socky, message):
    print(message)

if __name__ == "__main__":
    config = dotenv_values(".env")
    FTX = FTXClientHTTP(config['KEY'], config['SECRET'])
