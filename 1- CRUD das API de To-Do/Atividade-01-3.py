from funcoes import *

tipo_função()

while True:
    tipo = input("Digite a opção desejada: ")
    if tipo == "1":
        print("Você escolheu trabalhar com os usuarios")
        print()
        escolha_user()
        print()
        
    elif tipo == "2":
        print("você escolheu trabalhar com as tarefas dos usuarios")
        print()
        escolha_tasks()
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
        tipo_função()
        print()








