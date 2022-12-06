from ast import USub
from MyClasses import *
menu.tipo_função()
while True:
    tipo = input("Digite a opção desejada: ")
    if tipo == "1":
        print("Você escolheu trabalhar com os usuarios")
        print()
        menu.escolha_user()
        print()
        
    elif tipo == "2":
        print("você escolheu trabalhar com as tarefas dos usuarios")
        print()
        menu.escolha_tasks()
        print()
        
    elif tipo == "3":
        print()
        print("Sair do programa")
        print ("Obrigado por utilizar o programa")
        print()
        break

    else:
        print("Opção inválida")
        print("As opções são:")
        menu.tipo_função()
        print()
