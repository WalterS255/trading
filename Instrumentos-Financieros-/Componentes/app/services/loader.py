import psycopg2
import os

def load_to_database(data):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    for entry in data:
        cursor.execute(
            "INSERT INTO funding (id, amount, date, type) VALUES (%s, %s, %s, %s)",
            (entry["id"], entry["amount"], entry["date"], entry["type"])
        )
    conn.commit()
    cursor.close()
    conn.close()
def load_funding_data():
    from app.services.funding import get_funding_transactions
    from app.services.transformer import transform_funding_data
    from app.services.loader import load_to_database

    raw_data = get_funding_transactions()
    transformed_data = transform_funding_data(raw_data)
    load_to_database(transformed_data)
if __name__ == "__main__":
    load_funding_data()
    print("Datos de fondeo cargados exitosamente.")