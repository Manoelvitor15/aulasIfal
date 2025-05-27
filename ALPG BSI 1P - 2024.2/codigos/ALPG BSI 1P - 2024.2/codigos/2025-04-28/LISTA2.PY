import random as r

lista_vazia = []
lista_com_valores = [10, 20, 30]

print(lista_com_valores)
r.shuffle(lista_com_valores) #embaralha a lista
print(lista_com_valores)
print(r.choice(lista_com_valores)) #sorteia a lista