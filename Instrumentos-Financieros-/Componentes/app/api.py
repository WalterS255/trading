# app/api.py
from fastapi import FastAPI, HTTPException
from app.services.fetcher import fetch_stock_data
from app.services.transformer import transform_stock_data
from app.sources.market_client import MarketClient

market_client = MarketClient()

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
    
@app.get("/tarjetas/{symbol}")
def obtener_datos_tarjetas(symbol: str):
    resultado = market_client.get_daily_card(symbol)

    if not resultado:
        return {"error": "Datos no disponibles"}

    return resultado

@app.get("/dailylive/{symbol}")
def obtener_mercado_en_vivo(symbol: str):

    resultado = market_client.get_daily_info(symbol)

    if not resultado:
        return {"error": "Datos no disponibles"}

    return resultado

@app.get("/stocks")
def get_all_stocks():
    resultado = market_client.get_all_stocks()
    print("resultado: ", resultado)
    if not resultado:
        return {"error": "Datos no disponibles"}
    
    return resultado
