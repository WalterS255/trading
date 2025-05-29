from app.services.account import get_account_info
from app.services.funding import get_funding_transactions
from app.services.orders import create_order

if __name__ == "__main__":
    print("=== Info de la cuenta ===")
    print(get_account_info())

    print("\n=== Fondeo reciente ===")
    print(get_funding_transactions())

    print("\n=== Ejecutar orden ===")
    order = create_order(symbol="AAPL", qty=1)
    print(order)
