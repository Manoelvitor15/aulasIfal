def m2():
    print("inicio m2")
    lista = [1, 2, 3]
    try:
        for i in range(0,5):
            print(lista[i])
    except Exception as e:
        print(f"Erro em m2: {e}")
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