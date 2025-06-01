import schedule
import time
from app.sources.alpaca_client import obtener_precio_actual  # Asegúrate de que esta ruta sea correcta

def job():
    try:
        print("[INFO] Ejecutando tarea programada...")
        precio = obtener_precio_actual("AAPL")
        print(f"[INFO] Precio actual de AAPL: {precio}")
    except Exception as e:
        print(f"[ERROR] Error al ejecutar la tarea: {e}")

def iniciar_scheduler():
    print("[INFO] Inicializando el scheduler...")

    # Ejecuta `job` cada 10 segundos
    schedule.every(10).seconds.do(job)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Scheduler detenido por el usuario.")

if __name__ == "__main__":
    iniciar_scheduler()
