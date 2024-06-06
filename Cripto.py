import Matriz
from Matriz import determinanteMatriz
from Alfabeto import Alfabeto
from Alfabeto import Codigo
def recebeEntrada(lista):
    entrada = lista
    alfabeto = Alfabeto()
    listaPalavraCriptografada = []
    determinante = determinanteMatriz()
    chave = str(Codigo()) + "/" + str(determinante)

    for letra in entrada:

        if letra in alfabeto:
            indiceIncial = alfabeto.index(letra)
            novoIndice = int(indiceIncial + determinante) % len(alfabeto)
            listaPalavraCriptografada.append(alfabeto[novoIndice])

            palavraCriptografada = ''.join(listaPalavraCriptografada)

    #SAÍDA:
    #print(f'Matriz:  {Matriz.matrizCripto}')
    #print(f'Determinante:  {determinante}')
    print(f'Palavra Criptografada:  {palavraCriptografada}')
    print(f'Chave de criptografia:  {chave}')