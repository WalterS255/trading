# broadcast_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BroadcastClient:
    def __init__(self):
        self.base_url = os.getenv("BROADCAST_BASE_URL")
        self.headers = {
            "Authorization": f"Bearer {os.getenv('BROADCAST_API_KEY')}",
            "Content-Type": "application/json"
        }
    
    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            # Aquí podrías loggear o manejar errores de forma más sofisticada
            raise RuntimeError(f"HTTP Error: {e}, Response: {response.text}") from e
    
    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
    
    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)
    
    def get_account(self):
        return self.get("/account")
