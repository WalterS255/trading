from app.sources.alpaca_client import BroadcastClient

def fetch_funding_transactions():
    client = BroadcastClient()
    try:
        data = client.get("/v2/account/activities/FUNDING")
        return data
    except Exception as e:
        print(f"Error al obtener transacciones: {e}")
        return []
def fetch_account_info():
    client = BroadcastClient()
    try:
        data = client.get_account_info()
        return data
    except Exception as e:
        print(f"Error al obtener info de la cuenta: {e}")
        return {}
    
def fetch_stock_data(symbol):
    return {
        "symbol": symbol,
        "name": "Apple Inc.",
        "price": 52291,
        "change_percent": 0.25
    }