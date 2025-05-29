from app.services.account import get_account_info
from app.services.funding import get_funding_transactions
from app.services.orders import create_order

def main():
    print("=== Info de la cuenta ===")
    try:
        print(get_account_info())
    except Exception as e:
        print(f"Error al obtener la info de la cuenta: {e}")

    print("\n=== Fondeo reciente ===")
    try:
        print(get_funding_transactions())
    except Exception as e:
        print(f"Error al obtener transacciones de fondeo: {e}")

    print("\n=== Ejecutar orden ===")
    try:
        order = create_order(symbol="AAPL", qty=1)
        print(order)
    except Exception as e:
        print(f"Error al crear la orden: {e}")

if __name__ == "__main__":
    main()
