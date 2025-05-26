import random as r


numeroAleatorio = r.randint(1,60)
chutes = [] #iniciando a minha lista chamada chutes
while(True):
    chute = int(input("Qual seu chute? "))
    chuteJaFoiDado = False
    if(len(chutes) <= 0):
        chutes.append(chute)
    else:
        for i in range(0, len(chutes)): #percorrendo uma lista que não está vazia
            if(chute == chutes[i]):
                print("Esse chute já foi dado")
                chuteJaFoiDado = True
                break
        if(chuteJaFoiDado == False):
            chutes.append(chute)    

    if (chute == numeroAleatorio):
        print("Acertou!")
        print("Chutes dados:")
        for i in range(0, len(chutes)):
           print(chutes[i])
        break
    else:
        print("Errou!")    