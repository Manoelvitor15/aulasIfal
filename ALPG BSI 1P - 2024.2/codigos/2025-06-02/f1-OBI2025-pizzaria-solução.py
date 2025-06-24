#Recebendo a quantidade de pizzas grandes:
g=input("")
while True: 
    try:
        g=int(g)*8 #Calculando a quantidade de fatias
        break

    except ValueError:
        g=input("")

#Recebendo a quantidade de pizzas pequenas:
p=input("")
while True:
    try:
        p=int(p)*4 #Calculando a quantidade de fatias
        break
    except ValueError:
        p=input("")

print(f"{g+p-2}") #Imprimindo a quantidade de pessoas a serem convidadas
