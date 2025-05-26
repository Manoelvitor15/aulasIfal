cachorro_quente = 100
bauru_simples = 101
bauru_com_ovo = 102
hamburguer = 103
cheeseburguer = 104
refrigerante = 105

print("*******************************************")
print("*          Cardápio da Lanchonete         *")
print("*******************************************")
print("* ESPECIFICAÇÃO    |  CÓDIGO  |   PREÇO   *")
print("*******************************************")
print("* Cachorro quente  |    100   |  R$ 1.20  *")
print("*******************************************")
print("* Bauru simples    |    101   |  R$ 1.30  *")
print("*******************************************")
print("* Bauru com ovo    |    102   |  R$ 1.50  *")
print("*******************************************")
print("* Hambúrger        |    103   |  R$ 1.20  *")
print("*******************************************")
print("* Cheeseburguer    |    104   |  R$ 1.30  *")
print("*******************************************")
print("* Refrigerante     |    105   |  R$ 1.00  *")
print("*******************************************")
print()
codigo_item = int(input("Insira o código do lanche: "))
quant = int(input("Insira a quantidade de lanche: "))

if codigo_item == cachorro_quente:
    calc = quant * 1.20
    print(f"O valor total a ser pago pelo Cachorro quente é R$ {calc}")

elif  codigo_item == bauru_simples:
    calc = quant * 1.30
    print(f"O valor total a ser pago pelo Bauru Simples é R$ {calc}")

elif  codigo_item == bauru_com_ovo:
    calc = quant * 1.50
    print(f"O valor total a ser pago pelo Bauru com Ovo é R$ {calc}")
    
elif  codigo_item == hamburguer:
    calc = quant * 1.20
    print(f"O valor total a ser pago pelo Hambúrger é R$ {calc}")

elif  codigo_item == cheeseburguer:
    calc = quant * 1.30
    print(f"O valor total a ser pago pelo Cheeseburguer é R$ {calc}")

elif  codigo_item == refrigerante:
    calc = quant * 1.00
    print(f"O valor total a ser pago pelo Refrigerante é R$ {calc}")

else:
    print("ERRO!!")