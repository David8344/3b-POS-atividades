import requests
from getpass import getpass
import pandas as pd
import json
api_url = "https://suap.ifrn.edu.br/api/"

password = getpass("Senha: ")
user = '20191181110004'

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]

headers = {
    
    "Authorization": f'Bearer {token}'
}
resposta = requests.get(api_url + "/v2/minhas-informacoes/boletim/2022/1/", json=data, headers=headers)

data = json.loads(resposta.text)
dataf = pandas.DataFrame(data)

print(dataf)