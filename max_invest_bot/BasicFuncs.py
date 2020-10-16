import os
import sys
from dotenv import load_dotenv
sys.path.append('max-exchange-api-python3')
from max.client import Client


class BasicFuncs(object):
    """docstring for BasicFuncs."""

    def __init__(self):
        load_dotenv()
        API_KEY = os.getenv('API_KEY')
        SECRET_KEY = os.getenv('SECRET_KEY')
        self.PAIR = os.getenv('PAIR')
        self.AMOUNT = os.getenv('AMOUNT')
        self.client = Client(API_KEY, SECRET_KEY)

    def get_target_pair_current_price(self):
        current_k = self.client.get_public_k_line(self.PAIR, 1, 1)
        timestamp = current_k[0][0]
        open = current_k[0][1]
        high = current_k[0][2]
        low = current_k[0][3]
        close = current_k[0][4]
        volume = current_k[0][5]
        return timestamp, open, high, low, close, volume
