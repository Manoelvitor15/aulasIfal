#Elabore um algoritmo que dada a idade de um nadador, classica-o em uma
#das categorias:

# infantio A: 5 a 7 anos
# INfantio B: 8 a 10 anos
# juvenio A: 11 a 13 anos
# juvenio B: 14 a 17 anos
# adulto: maior que 18 anos

#idade menor que 5 anos não pode competir

idade = int(input("Informe a idade do nadador: "))

if (idade >= 5) and (idade <= 7):
    print("Categoria Infantil A")
elif (idade >= 8) and (idade <= 10):
    print("Categoria Infantil B")
elif (idade >= 11) and (idade <= 13):
    print("Categoria Juvenil A")
elif (idade >= 14) and (idade <= 17):
    print("Categoria Juvenil B")
elif idade >= 18:
    print("Categoria Adulto")
else:
    print(f"O competidor possui {idade} anos, com isso não pode competir.")