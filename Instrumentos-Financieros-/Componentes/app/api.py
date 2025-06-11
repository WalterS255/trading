# app/api.py
from fastapi import FastAPI, HTTPException
from app.services.fetcher import fetch_stock_data
from app.services.transformer import transform_stock_data
from app.sources.alpaca_market_client import AlpacaMarketClient

market_client = AlpacaMarketClient()

app = FastAPI()
@app.get("/")
def read_root():
    return {"mensaje": "¡API activa y funcionando!"}
@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    try:
        raw_data = fetch_stock_data(symbol)
        transformed = transform_stock_data(raw_data)
        return transformed
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/stocks")
def get_all_stocks():
    try:
        raw_data = fetch_stock_data()
        transformed = transform_stock_data(raw_data)
        return transformed
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/acciones/{symbol}")
def obtener_datos(symbol: str):
    resultado = market_client.get_daily_change(symbol)

    if not resultado:
        return {"error": "Datos no disponibles"}

    return resultado