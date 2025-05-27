quantNotas = 4
somaNotas = 0

while(quantNotas >= 1):
    nota = float(input("Insira a nota: "))

    if(nota < 0 or nota > 10):
        break
    
    somaNotas = somaNotas + nota
    quantNotas = quantNotas - 1

print(f"Média: {somaNotas / 4}")