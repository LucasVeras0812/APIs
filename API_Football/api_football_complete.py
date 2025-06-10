import requests
import pandas as pd

API_KEY = 'e7e98e2feaa7485cb39aabb3b5b6d3bc'
BASE_URL = 'https://api.football-data.org/v4/'
headers = {'X-Auth-Token': API_KEY}

"""
- Campeonato Brasileiro Série A (Código: BSA)
- Championship (Código: ELC)
- Premier League (Código: PL)
- UEFA Champions League (Código: CL)
- European Championship (Código: EC)
- Ligue 1 (Código: FL1)
- Bundesliga (Código: BL1)
- Serie A (Código: SA)
- Eredivisie (Código: DED)
- Primeira Liga (Código: PPL)"""

COMPETITION_ID = 'BSA' 

endpoint = f"competitions/{COMPETITION_ID}/standings"
url = BASE_URL + endpoint

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    standings_data = data['standings'][0]['table']

    df_classificacao = pd.DataFrame(standings_data)

    df_classificacao['teamName'] = df_classificacao['team'].apply(lambda x: x['name'])

    df_final = df_classificacao[[
        'position', 'teamName', 'playedGames', 'won', 'draw', 'lost', 'points', 'goalsFor', 'goalsAgainst', 'goalDifference'
    ]]

    df_final = df_final.rename(columns={
        'position': 'Posição',
        'teamName': 'Time',
        'won': 'V',
        'draw': 'E',
        'lost': 'D',
        'points': 'Pontos',
        'goalsFor': 'GP',
        'goalsAgainst': 'GC',
        'goalDifference': 'SG'
    })

    pd.set_option('display.max_rows', None)

    print(f"--- Tabela de Classificação: {data['competition']['name']} ---")
    print(df_final)

    print('\n--- Análise Rápida ---')

    time_mais_vitorias = df_final.loc[df_final['V'].idmax()]
    print(f"Time com mais vitórias: {time_mais_vitorias['Time']} ({time_mais_vitorias['V']} vitórias)")

    time_melhor_defesa = df_final.loc[df_final['GC'].idmax()]
    print(f"Time com a melhor defesa: {time_melhor_defesa['Time']} ({time_melhor_defesa['GC']} gols sofridos)")

    time_melhor_ataque = df_final[df_final['GP'].idmax()]
    print(f"Time com melhor ataque: {time_melhor_ataque['Time']} ({time_melhor_ataque['GP']} gols marcados)")

except requests.exceptions.HTTPError as err:
    print(f"Erro de HTTP: {err}")
except Exception as err:
    print(f"Ocorreu um erro: {err}")