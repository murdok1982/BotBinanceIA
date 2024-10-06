# trading/trader.py

from binance.client import Client
from config.config import BINANCE_API_KEY, BINANCE_SECRET_KEY

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def abrir_operacion(simbolo, cantidad, tipo):
    """Abre una orden de compra o venta en Binance."""
    if tipo == 'comprar':
        order = client.order_market_buy(symbol=simbolo, quantity=cantidad)
    elif tipo == 'vender':
        order = client.order_market_sell(symbol=simbolo, quantity=cantidad)
    return order
