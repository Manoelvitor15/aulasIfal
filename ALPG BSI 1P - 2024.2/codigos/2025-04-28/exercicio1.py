#um programa que irá sortear 6 números de 1 a 60. Os números não podem se repetir.

import random as r
numeros_sorteados = []
for i in range(1, 61):
        if numeros_sorteados <= 6:
            for i in range(1,7):
                print(r.choice(numeros_sorteados))