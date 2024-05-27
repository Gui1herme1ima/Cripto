#(Primeira letra, Segunda letra, terceira letra)
#(Quant. vogais, Letra c/ maior valor, Quant. Consoantes)
#(AntiPenultima letra, Penúltima Letra , Última letra)

matrizCripto = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def recebeLista(lista, quantVog, quantCons):
    print(quantVog)
    print(quantCons)
    matrizCripto[0][0] = int(lista[0]) #Primeira Letra
    matrizCripto[0][1] = int(lista[1]) #Segunda Letra
    matrizCripto[0][2] = int(lista[2]) #Terceira Letra

    matrizCripto[2][0] = int(lista[-3])  # AntiPenúltima Letra
    matrizCripto[2][1] = int(lista[-2])  # Penúltima Letra
    matrizCripto[2][2] = int(lista[-1])  # Última Letra

def imprimirMatriz():
    print(matrizCripto)