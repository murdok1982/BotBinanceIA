# main.py

import time
from data.data_fetcher import obtener_datos_mercado
from models.gpt_model import obtener_decision_gpt
from trading.trader import abrir_operacion
from config.config import TRADE_SYMBOL, TRADE_QUANTITY
from utils.logger import log_info, log_error

def trading_automatizado():
    """Función principal que ejecuta el trading automatizado."""
    while True:
        try:
            # Obtener datos de mercado
            datos_mercado = obtener_datos_mercado(TRADE_SYMBOL)
            log_info(f"Datos de mercado: {datos_mercado}")
            
            # Obtener la decisión del modelo GPT
            decision = obtener_decision_gpt(datos_mercado)
            log_info(f"Decisión del modelo GPT: {decision}")
            
            # Ejecutar la operación basada en la decisión
            if 'comprar' in decision.lower():
                abrir_operacion(TRADE_SYMBOL, TRADE_QUANTITY, 'comprar')
                log_info("Operación de compra ejecutada.")
            elif 'vender' in decision.lower():
                abrir_operacion(TRADE_SYMBOL, TRADE_QUANTITY, 'vender')
                log_info("Operación de venta ejecutada.")
            else:
                log_info("Decisión de mantener posición.")
            
            # Esperar antes de la próxima iteración
            time.sleep(60)  # Ejecutar cada minuto
        except Exception as e:
            log_error(f"Error en el ciclo de trading: {e}")

if __name__ == "__main__":
    trading_automatizado()
