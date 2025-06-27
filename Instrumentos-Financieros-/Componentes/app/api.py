# app/api.py
from fastapi import FastAPI, HTTPException, Request
from app.services.fetcher import fetch_stock_data
from app.services.transformer import transform_stock_data
from app.sources.market_client import MarketClient
from app.sources.broker_client import BrokerClient

from app.schemas import orderRequest, UserRequest, activityRequest


from typing import Optional, List

from pydantic import BaseModel

market_client = MarketClient()
broker_client = BrokerClient()

app = FastAPI()
@app.get("/")
def read_root():
    return {"mensaje": "¡API activa y funcionando!"}
@app.get("/api/stock/{symbol}")
def get_stock(symbol: str):
    try:
        raw_data = fetch_stock_data(symbol)
        transformed = transform_stock_data(raw_data)
        return transformed
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/market/tarjetas/{symbol}")
def obtener_datos_tarjetas(symbol: str):
    resultado = market_client.get_daily_card(symbol)

    if not resultado:
        return {"error": "Datos no disponibles"}

    return resultado

@app.get("/api/market/dailylive/{symbol}")
def obtener_mercado_en_vivo(symbol: str):

    resultado = market_client.get_daily_info(symbol)

    if not resultado:
        return {"error": "Datos no disponibles"}

    return resultado

@app.get("/api/market/stocks")
def get_all_stocks():
    resultado = market_client.get_all_stocks()
    #print("resultado: ", resultado)
    if not resultado:
        return {"error": "Datos no disponibles"}
    
    return resultado

@app.post("/api/broker/create_user")
async def create_user(data: UserRequest, request: Request):
    '''
    La fecha debe ir en formato YYYY-MM-DD
    "account_type": trading, custodial.
    founding_source: employment_income, investments, inheritance, business_income, savings, family.
    '''
    respuesta = broker_client.create_user(data, request.client.host)
    return respuesta.json()

@app.post("/api/broker/create_order")
async def create_order(order: orderRequest):
    '''
    side: buy, sell (se pueden añadir más).
    type:
        - market: Ejecuta la orden de inmediato
        - limit: Ejecuta la orden respecto a limites de precio, compra si baja al limite, vende si sube al limite
        - stop
        - stop_limit
    time in force: 
        - day: La orden es válida solo el día que se coloca.
        - gtc: La orden permanece activa hasta que se cancela o se ejecuta. (Good till Cancelled)
        - opg: La orden se ejecuta en la subasta de apertura. (On the Open)
        - cls: La orden se ejecuta en la subasta de cierre. (On the Close)
        - ioc: Ejecuta lo que pueda de inmediato. (Inmediate or Cancel)
        - fok: Ejecuta todo o nada. (Fill or Kill)
    '''
    respuesta = broker_client.create_order(order)
    return respuesta.json()

@app.post("/api/broker/view_user_trading_activity")
async def view_user_trading_activity(activity: activityRequest):
    respuesta = broker_client.view_user_trading_activity(activity)
    return respuesta.json()
