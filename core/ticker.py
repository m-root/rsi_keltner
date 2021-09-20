from settings import *
from numpy import mean

def ticker(pair):
    result = rest_client.ticker(pair)['result'][0]
    return [float(result['bid_price']), float(result['ask_price']), mean([float(result['bid_price']), float(result['ask_price'])])]


