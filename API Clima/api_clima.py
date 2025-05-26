import requests
import matplotlib.pyplot as plt
from datetime import datetime

#Chave da API
API_KEY = "e1a114dd533ba8e6f87e50169ffd078d"
HISTORICO_ARQUIVO = "historico_clima.txt"

def pegar_clima(cidade, chave_api):
    url = "https://api.openweathermap.org/data/2.5/weather"

    #Dicionário
    params = {
        "q": cidade,
        "appid": chave_api,
        "lang": "pt_br", #Linguagem
        "units": "metric" #Celsius 
    }

    resposta = requests.get(url, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()
        clima_formatado = (
        f"\n🗓 {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        f"\n☁️ Clima em {dados['name']}, {dados['sys']['country']}"
        f"\n🌡 Temperatura: {dados['main']['temp']}°C"
        f"\n😰 Sensação Térmica: {dados['main']['feels_like']}°C"
        f"\n💧 Umidade: {dados['main']['humidity']}%"
        f"\n🌬 Vento: {dados['wind']['speed']} m/s"
        f"\n📌 Descrição: {dados['weather'][0]['description'].capitalize()}"
    )

        print(clima_formatado)
        salvar_historico(clima_formatado)
        return dados['main']['temp'], dados['main']['feels_like'], dados['name']
    else:
        print("❌ Erro ao obter dados do clima. Verifique o nome da cidade e a sua chave da API.")
        return None, None, None
    
def salvar_historico(dados_formatados):
    with open(HISTORICO_ARQUIVO, 'a', encoding="utf-8") as arquivo:
        arquivo.write(dados_formatados)

def mostrar_historico():
    try:
        with open (HISTORICO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print('\n📜 Histórico de buscas:\n')
            print(conteudo)
    except FileNotFoundError:
        print('📭 Nenhum histórico encontrado.')

def gerar_grafico(temp, feels_like, cidade):
    labels = ['Temperatura', 'Sensação Térmica']
    valores = [temp, feels_like]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, valores, color=['skyblue', 'orange'])
    plt.title(f'Clima atual em {cidade}.')
    plt.ylabel('°C')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print('\n=== MENU CLIMA ===')
        print('1 - Ver clima atual')
        print('2 - Ver histórico de buscas')
        print('3 - Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            cidade = input('Digite o nome da cidade: ')
            temp, feels_like, nome_cidade = pegar_clima(cidade, API_KEY)
            if temp is not None:
                gerar_grafico(temp, feels_like, nome_cidade)
            elif escolha == '2':
                mostrar_historico()
            elif escolha == '3':
                print('👋 Encerrando o programa. Até logo!')
                break
            else:
                print('❗ Opção inválida. Tente novamente.')
# Inicia o menu
menu()