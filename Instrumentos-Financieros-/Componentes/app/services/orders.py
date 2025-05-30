from app.sources.alpaca_client import BroadcastClient

def create_order(symbol, qty, side="buy", type="market", time_in_force="gtc"):
    client = BroadcastClient()
    order = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    return client.post("/v2/orders", order)

def get_order_status(order_id):
    client = BroadcastClient()
    return client.get(f"/v2/orders/{order_id}")
def cancel_order(order_id):
    client = BroadcastClient()
    return client.delete(f"/v2/orders/{order_id}")