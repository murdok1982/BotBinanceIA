# data/data_fetcher.py

from binance.client import Client
from config.config import BINANCE_API_KEY, BINANCE_SECRET_KEY

# Inicializamos el cliente de Binance
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def obtener_datos_mercado(symbol):
    """Obtiene datos de mercado (velas) de Binance."""
    klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=50)
    return [{'open_time': k[0], 'open': k[1], 'high': k[2], 'low': k[3], 'close': k[4], 'volume': k[5]} for k in klines]
