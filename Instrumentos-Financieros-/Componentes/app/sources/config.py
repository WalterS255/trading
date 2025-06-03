import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError

# Cargar variables de entorno
load_dotenv()

def create_db_connection():
    """
    Crea y retorna una conexión a la base de datos PostgreSQL
    """
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        print("Conexión a PostgreSQL exitosa")
        return connection
    except OperationalError as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None

# Función para probar la conexión
def test_db_connection():
    conn = create_db_connection()
    if conn:
        cursor = conn.cursor()
        
        try:
            # Ejemplo: consultar traders
            cursor.execute("SELECT * FROM Trader LIMIT 5;")
            traders = cursor.fetchall()
            print("\nEjemplo de datos de Traders:")
            for trader in traders:
                print(trader)
                
        except Exception as e:
            print(f"Error al ejecutar consulta: {e}")
        finally:
            cursor.close()
            conn.close()
            print("\nConexión cerrada")

if __name__ == "__main__":
    test_db_connection()