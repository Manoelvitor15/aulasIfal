def validarNomeUsuario(nomeUsuario):
    if(len(nomeUsuario) >= 10 and nomeUsuario.find("@") >= 0 and nomeUsuario.find(".") >= 0):
        return True
    else:
        return False
    

def validarSenha(senha)
    if(senha.find("@") >= 0  and senha.find("!") >= 0 and len(senha) >= 7):
        return True
    else:
        return False


print("Acesso ao sistema")
print()
usuario = input("Usuário: ")
senha = input("Senha: ")

if(validarNomeUsuario(usuario) and validarSenha(senha)):
    print("Usuário e senha válidos")

else:
    print("Usuário ou senha inválidos")