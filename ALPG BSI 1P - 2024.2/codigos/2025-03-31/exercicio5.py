x = int(input("Insira um valor: "))
y = int(input("Insira um valor: "))
z = int(input("Insira um valor: "))

lados = x and y
comprimento = z

if (lados == x) and (lados == y) and (lados == z):
    print("Equiláteros: tem os comprimentos dos três lados iguais")

elif (lados == x) and (lados == y):
    print("Isósceles: tem os comprimentos de dois lados iguais")

elif (lados != x) and (lados != y) and (lados != z):
    print("Escaleno: tem os comprimentos dos três lados diferentes")

else:
    print("ERRO!!")