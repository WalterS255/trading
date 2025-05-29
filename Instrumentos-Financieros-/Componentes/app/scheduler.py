import schedule
import time
from app.sources.alpaca_client import obtener_precio_actual  # Ejemplo de función

def job():
    print("Ejecutando tarea programada...")
    precio = obtener_precio_actual("AAPL")  # Acción de ejemplo
    print(f"Precio actual de AAPL: {precio}")

def iniciar_scheduler():
    print("Inicializando el scheduler...")

    # Programa la tarea para que se ejecute cada 10 segundos
    schedule.every(10).seconds.do(job)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler detenido por el usuario.")

if __name__ == "__main__":
    iniciar_scheduler()
