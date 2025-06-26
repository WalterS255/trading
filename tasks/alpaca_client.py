# tasks/alpaca_client.py

from alpaca_trade_api.rest import REST
import os

ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL')

alpaca = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

def obtener_precio_actual(simbolo):
    try:
        trade = alpaca.get_latest_trade(simbolo)
        return float(trade.price)
    except Exception as e:
        return None
