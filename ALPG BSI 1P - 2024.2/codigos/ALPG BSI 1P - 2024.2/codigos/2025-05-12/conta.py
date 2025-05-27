"""
Operações brancárias:

Saldo
sacar(valor a sacar)
depositar(valor a depositar)
extrato

"""
opcao = 0;
valor_saque = ""
saldo = 0

def exibir_saldo():
    print(saldo)

def saque(saldo, valor_saque):
    print(saldo-valor_saque)
    



while(opcao != 5):
    print("Terminal Bancário")
    print("1. Saldo")
    print("2. Saque")
    print("3. Depositar")
    print("4. Extrato")
    print("5. Sair")

    opcao = int(input("Digite uma opção: "))

    if(opcao == 1):
        exibir_saldo()

    elif(opcao == 2):
        valor_saque = int(input("Digite o valor que você deseja sacar: "))


        print("** Saque **")

    elif(opcao == 3):
        deposito = int(input("Insira o valor que deseja depositar: "))
        saldo == deposito
        print("** Depositar **")

    elif(opcao == 4):
        print("Extrato")
    
    elif(opcao == 5):
        print("Encerrando o sistema")

    else:
        print("Opção inválida")