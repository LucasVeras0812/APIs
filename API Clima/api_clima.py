import requests 

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
        print(f"\n☁️ Clima em {dados['name']}, {dados['sys']['country']}")
        print(f"🌡 Temperatura: {dados['main']['temp']}°C")
        print(f"😰 Sensação Térmica: {dados['main']['feels_like']}°C")
        print(f"💧 Umidade: {dados['main']['humidity']}%")
        print(f"🌬 Vento: {dados['wind']['speed']} m/s")
        print(f"📌 Descrição: {dados['weather'][0]['description'].capitalize()}")

    else:
        print("Erro ao obter dados do clima. Verifique o nome da cidade e a sua chave da API.")

#Chave da API
API_KEY = "e1a114dd533ba8e6f87e50169ffd078d"

cidade = input("Digite o nome da cidade que você quer ver o clima completo: ")
pegar_clima(cidade, API_KEY)
