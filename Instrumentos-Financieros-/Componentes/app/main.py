from app.events.account_events import handle_account_state_event
from app.events.transfer_events import handle_transfer_event
from app.events.trade_events import handle_trade_event

# Simulación de eventos
if __name__ == "__main__":
    evento_cuenta = {
        "account_id": "abc123",
        "account_blocked": False,
        "cash_interest": 5.42,
        "trading_blocked": False
    }

    evento_transferencia = {
        "account_id": "abc123",
        "transfer_id": "tx999",
        "status_from": "pending",
        "status_to": "completed",
        "at": "2025-05-31T12:00:00Z"
    }

    evento_trade = {
        "account_id": "abc123",
        "at": "2025-05-31T12:05:00Z",
        "event": "filled",
        "event_id": "e1234",
        "timestamp": "2025-05-31T12:05:01Z",
        "order": {
            "id": "o789",
            "client_order_id": "cli456",
            "created_at": "2025-05-31T11:59:00Z",
            "updated_at": "2025-05-31T12:05:00Z",
            "expired_at": None,
            "submitted_at": "2025-05-31T12:00:00Z",
            "filled_at": "2025-05-31T12:05:00Z",
            "cancel_requested_at": None,
            "canceled_at": None,
            "failed_at": None,
            "qty": 10,
            "filled_qty": 10,
            "filled_avg_price": 142.5,
            "order_type": "limit",
            "stop_price": None,
            "status": "filled",
            "limit_price": 142.5,
            "stop_price": None,
            "extended_hours": False
        },
        "qty": 10,
        "Price": 142.5,
        "position_qty": 100,
        "execution_id": "exec123"
    }

    handle_account_state_event(evento_cuenta)
    handle_transfer_event(evento_transferencia)
    handle_trade_event(evento_trade)
# Este script simula la recepción de eventos de cuenta, transferencia y trade,
# y llama a las funciones correspondientes para manejarlos.
