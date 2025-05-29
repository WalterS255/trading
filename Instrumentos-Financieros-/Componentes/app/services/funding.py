import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from app.config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL
from app.sources.alpaca_client import AlpacaClient


def get_funding_transactions():
    client = AlpacaClient()
    return client.get("/v2/account/activities/FUNDING")
