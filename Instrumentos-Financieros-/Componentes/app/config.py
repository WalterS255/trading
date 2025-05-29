import os
from dotenv import load_dotenv

load_dotenv()

# Variables para Broadcast API
BROADCAST_API_KEY = os.getenv("BROADCAST_API_KEY")
BROADCAST_SECRET_KEY = os.getenv("BROADCAST_SECRET_KEY")
BROADCAST_BASE_URL = os.getenv("BROADCAST_BASE_URL")

# Variables para Alpaca API
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

# Validación básica (opcional pero recomendable)
if not BROADCAST_API_KEY or not BROADCAST_SECRET_KEY or not BROADCAST_BASE_URL:
    raise ValueError("Faltan variables de entorno para Broadcast API")

if not ALPACA_API_KEY or not ALPACA_SECRET_KEY:
    raise ValueError("Faltan variables de entorno para Alpaca API")
