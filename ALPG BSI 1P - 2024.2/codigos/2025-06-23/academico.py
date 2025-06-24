import util

notas = []


def adicionar_nota(nota):
    if(util.validar_nota(nota)):
        notas.append(nota)
    else:
        print("nota invalida")

def substituir_nota(posicao_substituir, nova_nota)

def calcular_media():
    soma_notas = 0
    if(len(notas) == 0):
        raise Exception("Lista está vazia")
    else:
        
        for i in notas:
            soma_notas += 1

        media = soma_notas / len(notas)
        return media
while(True):
    print("Opções: ")
    print("1. Adicionar notas")
    print("2. Verificar média")
    print("----------------------")
    print("3. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                print("Opção de adicionar")
                nota = float(input("Digite a nota: "))
                adicionar_nota(nota)
                input()
            case 2:
                print("Verificar notas")
                try:
                    print(calcular_media())
                except Exception as e:
                    print("Ocorreu um erro na verificação")
                input()
            case 3:
                print("Sair")
                input()
                break
            case _:
                print("Opção invalida")
                input()
    except ValueError as e:
        print("Valor invalido")
        input()
    except Exception as e:
        print("Um erro ocorreu")
        input()