'''
temos 10 estudantes.
soliciet as notas dos 10 estudantes.
se a media geral da turma for superior a 8.5, ganharam um brinde.
mas, se for encontradas 6 notas 10, nao precisa solicitar outras
notas, e ja ganharamo brinde.
'''

qtdEstudantes = 0
qtdNotas10 = 0
somaNotas = 0

while(qtdEstudantes <= 10):
    nota = float(input("Qual a nota? "))
    somaNotas = somaNotas + nota
    media = somaNotas / 10
    if(nota == 10):
        qtdNotas10 = qtdNotas10 + 1
    
    if(qtdNotas10 == 6):
        print("Ganharão um brinde porque já identificamos 6 notas 10")
        break

    qtdEstudantes = qtdEstudantes + 1  

if(qtdNotas10 < 6 and (media) > 8.5):
    print(f"Média: {media}, Ganharão um brinde")