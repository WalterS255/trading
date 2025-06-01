def handle_trade_event(event: dict):
    print("Evento de trade recibido:")
    print(f"Cuenta: {event['account_id']} - Evento: {event['event']}")
    print(f"Order ID: {event['order']['id']}")
    print(f"Cantidad ejecutada: {event['qty']} a precio {event['Price']}")
