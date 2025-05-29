from app.client.alpaca_client import AlpacaClient

def get_funding_transactions():
    client = AlpacaClient()
    return client.get("/v2/account/activities/FUNDING")
