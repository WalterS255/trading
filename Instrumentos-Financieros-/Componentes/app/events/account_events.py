def handle_account_state_event(event: dict):
    print("Evento de estado de cuenta recibido:")
    print(f"Cuenta: {event['account_id']}")
    print(f"Bloqueada: {event['account_blocked']}")
    print(f"Interés en efectivo: {event['cash_interest']}")
    print(f"Trading bloqueado: {event['trading_blocked']}")
