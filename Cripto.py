from Matriz import determinanteMatriz
from Alfabeto import Alfabeto
from Alfabeto import Codigo
def recebeEntrada(lista):
    entrada = lista
    alfabeto = Alfabeto()
    listaPalavraCriptografada = []

    chave = str(Codigo()) + "/" + str(determinanteMatriz())

    for letra in entrada:

        if letra in alfabeto:
            indiceIncial = alfabeto.index(letra)
            novoIndice = int(indiceIncial + determinanteMatriz()) % len(alfabeto)
            listaPalavraCriptografada.append(alfabeto[novoIndice])

            palavraCriptografada = ''.join(listaPalavraCriptografada)

    #SAÍDA:

    print(f'Palavra Criptografada:  {palavraCriptografada}')
    print(f'Chave de criptogarfia:  {chave}')