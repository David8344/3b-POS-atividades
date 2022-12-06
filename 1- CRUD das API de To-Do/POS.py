from urllib import response
import requests
api_url = "https://api.github.com/users/David8344"
response = requests.get(api_url)
print(response.json())

api_url2= "https://jsonplaceholder.typicode.com/todos/"
todo = {"user_Id" : 1, "tittle": "comprar farinha", "completed": "False"}
response = requests.post(api_url2, json=todo)
response = requests.get(api_url2)
print(response.json())
print(response.status_code)

api_url3= "https://jsonplaceholder.typicode.com/todos/3"
response = requests.get(api_url3)
print(response.json())

api_url4= "https://jsonplaceholder.typicode.com/post/3/comments"

response = requests.get(api_url4)
print(response.json())
