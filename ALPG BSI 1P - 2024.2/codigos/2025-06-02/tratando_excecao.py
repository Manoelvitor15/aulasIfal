def m2():
    print("inicio m2")
    lista = [1, 2, 3]
    try:
        inteiro = int(input("Digite um número inteiro: "))
        print(10/0)
        for i in range(0,5):
            print(lista[i])
    except ValueError as e:
        print("Erro em m2")
    except IndexError:
        print("Tentando acessar um indice que não existe!")
    except Exception:
        print("Erro genérico")
    print("fim m2")
def m1():
    print("Inicio m1")
    m2()
    print("fim m1")

def main():
    print("Inicio main")
    m1()
    print("fim main")

    
main()