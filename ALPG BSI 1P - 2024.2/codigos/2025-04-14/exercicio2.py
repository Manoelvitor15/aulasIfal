"""
encontrando numeros primos de 1 a 50

"""

numero = 1
quantidade_primos = 0
total_divisores = 0
divisor = 0
while(numero <= 50):
    divisor = 1
    total_divisores = 0

    while divisor <= numero:
        if numero % divisor == 0:
            total_divisores += 1
        divisor += 1

    if total_divisores == 2:
        print(numero, "é primo")
        quantidade_primos += 1

    else:
        print(numero)

    numero += 1

print("Quantidade de números primos de  1 a 50: ", quantidade_primos)