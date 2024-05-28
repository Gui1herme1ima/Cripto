from Matriz import determinanteMatriz
from Alfabeto import definirAlfabeto
from Alfabeto import definirChave
def recebeEntrada(lista):
    entrada = lista
    alfabeto = definirAlfabeto()
    chave = definirChave()
    listaPalavraCriptografada = []

    for letra in entrada:

        if letra in alfabeto:
            indiceIncial = alfabeto.index(letra)
            novoIndice = int(indiceIncial + determinanteMatriz()) % len(alfabeto)
            listaPalavraCriptografada.append(alfabeto[novoIndice])

            palavraCriptografada = str(listaPalavraCriptografada)

    print(f' A palavra criptografada é: {palavraCriptografada}')