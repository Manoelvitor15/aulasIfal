opcao = 0

def menu():
    global menu
    while(opcao != 3):
        print("Opções: ")
        print("1. Soma")
        print("2. Subtração")
        print("---------------")
        print("3. Sair")
        opcao = int(input("Escolha uma opção de 1 a 3: "))

