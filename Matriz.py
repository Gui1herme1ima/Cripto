#(Primeira letra, Segunda letra, terceira letra)
#(Quant. vogais, Letra c/ maior valor, Quant. Consoantes)
#(AntiPenultima letra, Penúltima Letra , Última letra)
import random

matrizCripto = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def recebeLista(lista, quantVog, quantCons, MaiorLetra):
    matrizCripto[0][0] = int(lista[0])  # a11 - Primeira Letra
    matrizCripto[0][1] = int(lista[1])  # a12 - Segunda Letra
    matrizCripto[0][2] = int(lista[2])  # a13 - Terceira Letra
    matrizCripto[1][0] = int(quantVog)  # a21- Quantidade Vogais
    matrizCripto[1][1] = int(MaiorLetra)  # a22- Maior Letra
    matrizCripto[1][2] = int(quantCons)  # a23 - Quantidade Consoantes
    matrizCripto[2][0] = int(lista[-3])  # a31 - AntiPenúltima Letra
    matrizCripto[2][1] = int(lista[-2])  # a32 - Penúltima Letra
    matrizCripto[2][2] = int(lista[-1])  # a33 - Última Letra

def determinanteMatriz():
    from Alfabeto import tamanhoAlfabeto
    #a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a13*a22*a31 - a11*a23*a32 - a12*a21*a33
    a11a22a33 = matrizCripto[0][0] * matrizCripto[1][1] * matrizCripto[2][2]
    a12a23a31 = matrizCripto[0][1] * matrizCripto[1][2] * matrizCripto[2][0]
    a13a21a32 = matrizCripto[0][2] * matrizCripto[1][0] * matrizCripto[2][1]
    a13a22a31 = matrizCripto[0][2] * matrizCripto[1][1] * matrizCripto[2][0]
    a11a23a32 = matrizCripto[0][0] * matrizCripto[1][2] * matrizCripto[2][1]
    a12a21a33 = matrizCripto[0][1] * matrizCripto[1][0] * matrizCripto[2][2]

    determinante = (a11a22a33 + a12a23a31 + a13a21a32 - a13a22a31 - a11a23a32 -a12a21a33)

    if determinante == 0:
        determinante = random.randint(-tamanhoAlfabeto+1, tamanhoAlfabeto-1)

    return determinante

def imprimirMatriz():
    print(f'Matriz: {matrizCripto}')
    print(f'Determinante: {determinanteMatriz()}')
