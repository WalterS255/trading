import os
import requests

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
}

def obtener_info_accion(ticker):
    url = f"{ALPACA_BASE_URL}/v2/stocks/{ticker}/quote"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener info de {ticker}: {response.status_code} {response.text}")

def realizar_orden(ticker, cantidad, tipo='buy'):
    url = f"{ALPACA_BASE_URL}/v2/orders"
    data = {
        "symbol": ticker,
        "qty": cantidad,
        "side": tipo,
        "type": "market",
        "time_in_force": "gtc"
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al realizar orden: {response.status_code} {response.text}")
