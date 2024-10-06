# models/gpt_model.py

import requests
from config.config import GPT_API_KEY, GPT_API_URL

def obtener_decision_gpt(datos_mercado):
    """Envía los datos del mercado al modelo GPT y obtiene una decisión."""
    prompt = {
        'prompt': f"Analiza los siguientes datos de mercado: {datos_mercado}. ¿Debo comprar, vender o mantener?",
        'model': 'text-davinci-003',  # Ajusta según el modelo GPT específico
        'max_tokens': 150
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GPT_API_KEY}'
    }
    
    response = requests.post(GPT_API_URL, json=prompt, headers=headers)
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()
