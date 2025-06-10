import requests
import os 

API_KEY = 'e7e98e2feaa7485cb39aabb3b5b6d3bc'

BASE_URL = 'https://api.football-data.org/v4'

headers = {'X-Auth-Token': API_KEY}

endpoint = 'competitions'
url = f'{BASE_URL}/{endpoint}'

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    print("Conexão bem sucedida! Competições disponíveis:")
    for competition in data['competitions'][:10]:
        print(f"- {competition['name']} (Código: {competition['code']})")

except requests.exceptions.HTTPError as err:
    print(f"Erro de HTTP: {err}")
    print("--- DICAS ---")
    print("1. Verifique se sua APY_KEY está corretar.")
    print("2. O plano gratuito tem um limite de 10 chamadas por minuto")
except requests.exceptions.RequestException as err:
    print(f"Erro de conexão: {err}")


