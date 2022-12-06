
from urllib import response
import requests
api_users = "https://jsonplaceholder.typicode.com/users/"
api_tasks = "https://jsonplaceholder.typicode.com/todos/"

class usuario:

    def ler():
        response = requests.get(api_users)
        usuarios = response.json()
        for usuario in usuarios:
            print(usuario["id"], usuario["name"])
    def criar():
        nome = input("digite o nome do usuario")
        username = input("digite o nome de usuario")
        email = input("digite o email do usuario")
        response = requests.post(api_users, data = {"name": nome, "username": username, "email": email})
        if response.status_code == 201:
            print("usuario criado")
        else:
            print("não foi possivel criar o usuario")
    def atualizar():
        id = input("Digite o id do usuário: ")
        response = requests.get(api_users + id)
        if response.status_code == 200:
            
            user =response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print("Digite os novos dados do usuário")
            nome = input("Digite o nome do usuário: ")
            username = input("Digite o username de usuário: ")
            email = input("Digite o email do usuário: ")
            response = requests.put(api_users + id, data = {"name": nome, "username": username, "email": email})
            print()
            print(response.status_code)
            print()
    def deletar():
        id = input("Digite o id do usuário: ")
        response = requests.get(api_users + id)
        if response.status_code == 200:
            user =response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print()
            print("Deseja realmente deletar o usuário?")
            opcao = input("Digite 1 para sim e 2 para não: ")
            if opcao == "1":
                response = requests.delete(api_users + id)
                print()
                print(response.status_code)
                print()
            elif opcao == "2":
                print("Usuário não deletado")
                print()
            else:
                print("Opção inválida")
                print()
        else:
            print("Usuário não encontrado")
            print()


class tarefas:
    def ler():
        id = input("Digite o id do usuário: ")
        response = requests.get(api_users + id +"/todos" )
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                print("Titulo: ", task["title"])
                print("Status: ", task["completed"])
    

    def criar():
        id = input("digite a id do usuario que a tarefa pertence ")
        titulo = input("digite o titulo da tarefa ")
        status = input("digite se a tarefa esta completa ou não (True|False) ")
        response = requests.post(api_users + id +"/todos", data = {"userId": id, "title": titulo, "status": status})
        if response.status_code == 201:
            print("tarefa criada")
    

    def atualizar():
        id = input("Digite o id da tarefa: ")
        response = requests.get(api_tasks + id)
        if response.status_code == 200:
            task =response.json()
            print("Tarefa com o título: [", task["title"], "] encontrada")
            print("Status: ", task["completed"])
            print()
            print()
            print("Digite os dados da tarefa")
            titulo = input("Digite o título da tarefa: ")
            status = input("Digite o status da tarefa: ")
            user = input("digite o id do usuario que ira realizar a tarefa ")
            response = requests.put(api_tasks + id, data = {"userId": user, "title": titulo, "completed": status})
            print()
            print(response.status_code)
            print()
    def deletar():
        print()
        id_tasks = input("Digite o id da tarefa: ")
        response = requests.get(api_tasks + id_tasks)
        if response.status_code == 200:
            task =response.json()
            print("Tarefa com o título: [", task["title"], "] encontrada")
            print("Status: ", task["completed"])
            print()
            print("Deseja realmente deletar a tarefa?")
            opcao = input("Digite 1 para sim e 2 para não: ")
            if opcao == "1":
                response = requests.delete(api_tasks + id_tasks)
                print()
                print(response.status_code)
                print()
            elif opcao == "2":
                print("Tarefa não deletada")
                print()
            else:
                print("Opção inválida")
                print()
        else:
            print("Tarefa não encontrada")
            print()
        return 0
class listagem:
    def listar_user():

        response = requests.get(api_users)
        if response.status_code == 200:
            usuarios = response.json()
            for usuario in usuarios:
                print(usuario["id"], usuario["name"])



    def listar_tasks():
        response = requests.get(api_tasks)
        if response.status_code == 200:
            todos = response.json()
            for todo in todos:
                print(todo["id"], todo["title"])

class menu:
               
    def crud_users():
        print()
        print("Digite 1 para criar usúarios")
        print("Digite 2 para ler usúarios")
        print("Digite 3 atualizar usúarios")
        print("Digite 4 para deletar usúarios")
        print()
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            usuario.criar()
        elif opcao == 2:
            usuario.ler()
        elif opcao == 3:
            usuario.atualizar()
        elif opcao == 4:
            usuario.deletar()
        else:
            print("opção invalida")
            print("as opções disponiveis são:")
            menu.crud_users()

    def crud_tasks():
        print()
        print("Digite 1 para criar tarefas para usúarios")
        print("Digite 2 para ler tarefas dos usúarios")
        print("Digite 3 atualizar tarefas dos usúarios")
        print("Digite 4 para deletar tarefas dos usúarios")
        print()
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            tarefas.criar()
        elif opcao == 2:
            tarefas.ler()
        elif opcao == 3:
            tarefas.atualizar()
        elif opcao == 4:
            tarefas.deletar()
        else:
            print("opção invalida")
            print("as opções disponiveis são:")
            menu.crud_tasks()
    def tipo_função():
        print()
        print ("qual tipo de tarefa deseja realizar")
        print("Digite 1 para realizar as funções com os usuarios")
        print("Digite 2 para realizar as funções com as tarefas do usuario")
        print("Digite 3 para fechar o programa")
    def escolha_user():
        print()
        print ("qual tarefa deseja realizar")
        print("Digite 1 para listar os usuarios")
        print("Digite 2 para criar, ler, atualizar ou deletar os usúarios")
        print()
        escolha = int(input("Digite a opção desejada: "))
        if escolha == 1:
            listagem.listar_user()
        elif escolha == 2:
            menu.crud_users()
        else:
            print("Opção invalida")
            print("as opções disponiveis são:")
            menu.escolha_user()

    def escolha_tasks():
        print()
        print ("qual tarefa deseja realizar")
        print("Digite 1 para listar as tarefas do usuario")
        print("Digite 2 para criar, ler, atualizar ou deletar tarefas dos usúarios")
        print()
        escolha = int(input("Digite a opção desejada: "))
        if escolha == 1:
            listagem.listar_tasks()
        elif escolha == 2:
            menu.crud_tasks()
        else:
            print("Opção invalida")
            print("as opções disponiveis são:")
            menu.escolha_tasks()


