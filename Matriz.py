#(Primeira letra, Segunda letra, terceira letra)
#(Quant. vogais, Letra c/ maior valor, Quant. Consoantes)
#(AntiPenultima letra, Penúltima Letra , Última letra)

matrizCripto = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def recebeLista(lista, quantVog, quantCons, MaiorLetra):
    matrizCripto[0][0] = int(lista[0])  # Primeira Letra
    matrizCripto[0][1] = int(lista[1])  # Segunda Letra
    matrizCripto[0][2] = int(lista[2])  # Terceira Letra
    matrizCripto[1][0] = int(quantVog)  # Quantidade Vogais
    matrizCripto[1][1] = int(MaiorLetra)  # Maior Letra
    matrizCripto[1][2] = int(quantCons)  # Quantidade Consoantes
    matrizCripto[2][0] = int(lista[-3])  # AntiPenúltima Letra
    matrizCripto[2][1] = int(lista[-2])  # Penúltima Letra
    matrizCripto[2][2] = int(lista[-1])  # Última Letra


def imprimirMatriz():
    print(matrizCripto)
