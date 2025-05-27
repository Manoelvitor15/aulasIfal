print("Lista de notas")


notas = []

for i in range(0, 4):

    nota = float(input(f"Digite a {i+1}º nota: "))
    notas.append(nota)

print("Notas digitadas:")
print(notas)

opcao = input("Deseja corrigir uma nota? S / N ")

if(opcao.upper() == "S"):
    print("Vamos corrigir a nota!")

    posicao = int(input("Qual a nota que deseja corrigir? (1 a 4)"))

    del(notas[posicao-1])

    print(notas)