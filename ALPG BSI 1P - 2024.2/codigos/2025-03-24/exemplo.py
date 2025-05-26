print("Cadastrar Usuário e senha")
print()
nome = input("Digite Usuário: ")
senha1 = input("Digite uma senha: ")
senha2 = input("Confirme sua senha: ")

if nome != "":
    print("Usuário cadastrado!")
    if senha1 != "":
    
        if senha1 == senha2:
            print(f"{nome} seu usuario foi cadastrado")
        else:
            print("senha incorreta!")

    else:
        print("senha nao pode ser vazio")
else:
    print("usuario nao cadastrado")
    print("senha incorreta!")