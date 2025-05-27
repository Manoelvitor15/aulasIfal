#Q1. Faça um algoritmo que lê dois números, e verifica se os dois números são iguais. 
#Se forem iguais, escrever "São iguais", se não, escrever "Não são iguais".

#print("verifica se os dois números são iguais")
#print()
#senha1 = int(input("Digite um número: "))
#senha2 = int(input("Confirme seu número: "))

#if senha1 == senha2:
    #print("São iguais!")

#else:
    #print("Não são iguais!")



#Q2. Faça um algoritmo que lê dois números, e informa se são iguais. 
#Se não forem iguais, informar qual é o maior e qual é o menor número.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))

if numero1 == numero2:
    print("São iguais!")

else:
    if numero1 > numero2:
        print(f"{numero1} é maior que {numero2}")
        print(f"{numero2} é menor que número {numero1}")

    #elif


#Q3. Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, 
#solicita o nome do usuário, e a senha. Depois, pede que o usuário confirme novamente 
#a senha. O sistema deverá verificar se as senhas digitadas são iguais. 
#Se forem iguais, informar que o cadastro está correto. Se não forem iguais, informar 
#que o cadastro não foi realizado porque as senhas não conferem.

#print("Cadastrar Usuário e senha")
#nome = input("Digite Usuário: ")
#senha1 = input("Digite uma senha: ")
#senha2 = input("Confirme sua senha: ")

#if senha1 == senha2:
    #print(f"{nome} voce está cadastrado em sistema.")

#else:
    #print(f"falha ao efetuar cadastro, verificar se senhas digitadas são iguais.")