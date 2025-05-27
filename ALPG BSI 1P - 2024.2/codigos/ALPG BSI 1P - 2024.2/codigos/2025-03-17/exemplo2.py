senha_antiga = 112233
senha_digitada = int(input("Digite uma nova senha: "))
senha_armazenada = 0
if senha_digitada  != senha_antiga:
    print("Senha alterada com sucesso!")
    senha_armazenada = senha_digitada