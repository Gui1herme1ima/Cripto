import Alfabeto
palavra = "teste"
def descriptografar(alfabeto, determinante, palavraCriptografada):

    listaPalavraDescriptografada = []
    listaPalavraCriptografada = list(palavraCriptografada)

    for caractere in listaPalavraCriptografada:

        if caractere in alfabeto:
            indiceCriptografado = alfabeto.index(caractere)
            indiceIncial = int((indiceCriptografado - determinante) % len(alfabeto))
            listaPalavraDescriptografada.append(alfabeto[indiceIncial])

            palavraDescriptografada = ''.join(listaPalavraDescriptografada)

    print(f'A palavra descriptografada é: {palavraDescriptografada}')

def palavraCriptografada(palavraCriptografada):
    global palavra
    palavra = palavraCriptografada


def Chave(chave):
    global partes, codigo, determinante, deteminanteEncontrada
    deteminanteEncontrada = False
    if not "/" in chave:
        chaveIncorreta()
    else:
        partes = chave.split('/')

    if len(partes) > 1:
        numero_str = partes[1]
        if numero_str.lstrip('-').isdigit():
            numero = int(numero_str)
            codigo = partes[0]
            determinante = numero
            verificarChave(codigo, determinante)
    else:
        chaveIncorreta()
def verificarChave(codigo, determinante):
    global palavra
    chaveEncontrada = False
    if codigo in Alfabeto.codigos0:
        descriptografar(Alfabeto.alfabeto0,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos1:
        descriptografar(Alfabeto.alfabeto1,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos2:
        descriptografar(Alfabeto.alfabeto2,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos3:
        descriptografar(Alfabeto.alfabeto3,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos4:
        descriptografar(Alfabeto.alfabeto4,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos5:
        descriptografar(Alfabeto.alfabeto5,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos6:
        descriptografar(Alfabeto.alfabeto6,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos7:
        descriptografar(Alfabeto.alfabeto7,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos8:
        descriptografar(Alfabeto.alfabeto8,determinante,palavra)
        chaveEncontrada = True
    elif codigo in Alfabeto.codigos9:
        descriptografar(Alfabeto.alfabeto9,determinante,palavra)
        chaveEncontrada = True
    if not chaveEncontrada:
        chaveIncorreta()
def chaveIncorreta():
    chave = input("Chave incorreta!\n"
                  "Digite uma chave válida: ")
    Chave(chave)