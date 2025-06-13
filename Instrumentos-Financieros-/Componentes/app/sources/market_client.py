# alpaca_market_client.py
import os
from datetime import datetime, timedelta
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from polygon import RESTClient

from dotenv import load_dotenv

load_dotenv()

class MarketClient:
    def __init__(self):
        self.alpaca = StockHistoricalDataClient(
            os.getenv("ALPACA_API_KEY"),
            os.getenv("ALPACA_SECRET_KEY")
        )

        self.polygon = RESTClient(os.getenv("POLYGON_API_KEY"))
    
    def get_daily_change(self, symbols: list[str]):
        hoy = datetime.now().date()
        ayer = hoy - timedelta(days=5)  # margen por días no hábiles

        params = StockBarsRequest(
            symbol_or_symbols=symbols,
            timeframe=TimeFrame.Day,
            start=ayer,
            end=hoy
        )

        bars = self.alpaca.get_stock_bars(params).df 
         
        resultados = []        
        if bars.empty:
            return resultados  # Lista vacía si no hay datos

        # Agrupar por símbolo usando el índice de nivel 0
        for symbol, df_symbol in bars.groupby(level=0):
            if len(df_symbol) < 2:
                continue  # Ignora si no hay suficientes datos            

            ultimo = df_symbol.iloc[-1]["close"]
            anterior = df_symbol.iloc[-2]["close"]
            variacion = ((ultimo - anterior) / anterior) * 100

            details = self.polygon.get_ticker_details(symbol)
            companyName = details.name
            tokenLogo = os.getenv("LOGO_API_KEY")

            resultados.append({
                "icono": f"https://img.logo.dev/ticker/{symbol}?token={tokenLogo}",
                "titulo": companyName,
                "ticker": symbol,
                "valor": round(ultimo, 2),
                "diferencia": round(variacion, 2)
            })

        return resultados
