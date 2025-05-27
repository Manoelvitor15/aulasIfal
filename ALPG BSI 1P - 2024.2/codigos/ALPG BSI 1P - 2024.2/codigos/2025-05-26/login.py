def validarNomeUsuario(nomeUsuario):
    return  len(nomeUsuario) >= 10 and "@" in nomeUsuario and "." in nomeUsuario
    

def validarSenha(senha)
    return "!" in senha and "@" in senha and len(senha) >= 7

print("Acesso ao sistema")
print()
usuario = input("Usuário: ")
senha = input("Senha: ")

if(validarNomeUsuario(usuario) and validarSenha(senha)):
    print("Usuário e senha válidos")

else:
    print("Usuário ou senha inválidos")