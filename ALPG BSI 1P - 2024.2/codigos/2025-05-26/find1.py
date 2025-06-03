palavra = "banana"
tamanhoPalavra = len(palavra)


posicaoPrimeiroAna = print(palavra.find("ana"))
print(posicaoPrimeiroAna)

posicaoSegundoAna = palavra.find("ana", posicaoPrimeiroAna+2)
print(posicaoSegundoAna)

#quando não encontra, retorna -1
print(palavra.find("o"))