# utils/logger.py

import logging

# Configuración básica del logger
logging.basicConfig(
    filename="bot_binance.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
