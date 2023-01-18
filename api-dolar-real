#bibliotecas
import requests
import json

#requisicao web
web = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")

#leitura json
cotacao = web.json()

#print
print("Moeda: " + cotacao["USD"]["name"] + "\n" +  
      "Valor atual: R$ " + cotacao["USD"]["bid"] + '\n'+ 
      cotacao["USD"]["create_date"] )
