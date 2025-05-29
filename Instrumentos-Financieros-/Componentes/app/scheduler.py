import schedule
import time
from etl.extractor import AlpacaExtractor
from etl.transformer import Transformer
from etl.loader import Loader

def job():
    print("Ejecutando pipeline ETL...")
    
    extractor = AlpacaExtractor()
    transformer = Transformer()
    loader = Loader()

    raw_data = extractor.get_last_prices("AAPL", limit=5)
    transformed = transformer.transform(raw_data)
    loader.load(transformed)

    print("Proceso ETL completado.")

# Programa la tarea cada 10 minutos (por ejemplo)
schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    print("Iniciando el scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)
