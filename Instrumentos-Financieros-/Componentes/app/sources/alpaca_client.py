import requests
from app.config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

class AlpacaClient:
    def __init__(self):
        self.base_url = ALPACA_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "APCA-API-KEY-ID": ALPACA_API_KEY,
            "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
        })

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
