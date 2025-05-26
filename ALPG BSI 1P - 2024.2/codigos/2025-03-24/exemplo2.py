# Problema: Tentar acertar um número secreto.
# Solocitar o chute do usuário
# Se o chute dado for igual ao número. Informe que ele acertou o chute
#se não for igual, verifique e informe se o chute dado foi maior ou menor que o numero secreto.

numero_secreto = 23
print("Adivinhe um número de 1 a 100")
chute = int(input("Qual o chute? "))

if chute == numero_secreto:
    print("Acertou!")

elif chute > numero_secreto:
    print("Chute foi maior!")

else:
    print("Chute foi menor!")