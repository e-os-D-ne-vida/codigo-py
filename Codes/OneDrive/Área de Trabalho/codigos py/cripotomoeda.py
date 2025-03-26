import requests
import smtplib

def acompanhar_varias_criptomoedas(criptomoedas, moeda):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(criptomoedas)}&vs_currencies={moeda}"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        for cripto in criptomoedas:
            preco = dados[cripto][moeda]
            print(f"O preço do {cripto.capitalize()} em {moeda.upper()} é: {preco:.2f}")
    else:
        print("Erro ao acessar a API:", response.status_code)

criptomoedas = ["bitcoin", "ethereum", "dogecoin" , "litecoin", "ripple"]
moeda = "brl"
acompanhar_varias_criptomoedas(criptomoedas, moeda)


