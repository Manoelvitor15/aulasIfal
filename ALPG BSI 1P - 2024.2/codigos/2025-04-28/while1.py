opcao = 0;

while(opcao != 3):
    print("Terminal Bancário")
    print("1. Saldo")
    print("2. Saque")
    print("3. Sair")

    opcao = int(input("Digite uma opção: "))

    if(opcao == 1):
        print("** Saldo **")
    elif(opcao == 2):
        print("** Saque **")
    elif(opcao == 3):
        print("Encerrando o sistema")

    else:
        print("Opção inválida")