
from app.sources.alpaca_client import BroadcastClient

client = BroadcastClient()

def get_account_info():
    return client.get_account_info()