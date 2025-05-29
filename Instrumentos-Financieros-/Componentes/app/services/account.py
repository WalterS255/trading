from app.sources.alpaca_client import AlpacaClient

def get_account_info():
    client = AlpacaClient()
    return client.get("/v2/account")
