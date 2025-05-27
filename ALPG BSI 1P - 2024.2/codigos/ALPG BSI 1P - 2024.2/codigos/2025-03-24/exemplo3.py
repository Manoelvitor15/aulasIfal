#solicita do usuario para que ele digite um numero de 1 a 7, de modo que o numero
#digitado representa o dia da semana, começando por domingo
#se o numero nao estiver no intervalo de 1 a 7, informe que é um numero invalido

numero = int(input("digite um numero de 1 a 7, de modo que o numero digitado representa o dia da semana, começando por domingo"))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Terça")
elif numero == 4:
    print("Quarta")
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta")
elif numero == 7:
    print("Sabado")
else:
    print("Numero invalido!")

