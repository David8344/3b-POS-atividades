import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = "david8344"
password = 'token'

print("Digite 1 para ver seus seguidores")
print("Digite 2 para seguir um usuario")
print("Digite 3 para parar de seguir um usuario")
print("Digite 4 para ver quem segue Maike")

 
pergunta = int(input('digite a opção escolhida'))
 

if pergunta == 1:
    response = requests.get('https://api.github.com/user/followers',
        auth = HTTPBasicAuth(user, password))
 
elif pergunta == 2:
    response = requests.put('https://api.github.com/user/following'+'/DUARTEzinho',
        auth = HTTPBasicAuth(user, password))

elif pergunta == 3:
    response = requests.delete('https://api.github.com/user/following'+'/DUARTEzinho',
        auth = HTTPBasicAuth(user, password))

elif pergunta == 4:
    response = requests.get('https://api.github.com/users/dvcirilo/following/maikerosa',
        auth = HTTPBasicAuth(user, password))
 
  
print(response[('login')])

print(response)