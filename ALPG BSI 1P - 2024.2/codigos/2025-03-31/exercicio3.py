#Q3. Escreva um algoritmo que leia o nome e as 
#três notas obtidas por um aluno durante o semestre. Calcular 
#a sua média (aritmética), informar o nome e o resultado final: 
#Aprovado (media >= 7), Reprovado (media <= 5), 
#ou em Recuperação (media entre 5.1 a 6.9).


nome_aluno = input("Digite o nome do aluno: ")
print()
nota1 = float(input("Infome a 1° nota: "))
nota2 = float(input("Infome a 2° nota: "))
nota3 = float(input("Infome a 3° nota: "))
nota4 = float(input("Infome a 4° nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"{nome_aluno} você está aprovado com média {media}")

elif media <= 5:
    print(f"{nome_aluno} você está reprovado com média {media}")
    
elif (media >= 5.1) and (media <= 6.9):
    print(f"{nome_aluno} você está recuperação com média {media}")

else:
    print("Faltou digitar um nota!")