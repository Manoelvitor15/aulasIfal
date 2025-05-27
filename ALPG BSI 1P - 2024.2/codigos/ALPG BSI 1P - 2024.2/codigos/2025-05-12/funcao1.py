nome_usuario = ""
senha = ""

def abertura_cadastro_sistema():
    global nome_usuario, senha
    print("Sistema de Cadastro de Usuário")
    print("Data de hoje: 12/05/2025")
    nome_usuario = input("Digite o nome do usuário de cadastro: ")
    senha = input("Digite a senha de cadastro: ")

def validar_nome_usuario():
    print("Válidando usuário...")

abertura_cadastro_sistema()


if(nome_usuario != "" and senha != ""):
    if("@" in nome_usuario):
        print("Nome de usuário válido")
    else:
        print("Nome de usuário inválido")

    if(senha.isdigit() and len(senha) > 4):
        print("Senha válida")
    else:
        print("Senha inválida")


else:
    print("Senha e/ou nome do usuário não podem ser vazios")