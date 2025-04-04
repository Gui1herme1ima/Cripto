def posicaoNoAlfabeto(lista):
    listaPosicao = []
    for char in lista:
        char = char.upper()

        if char.isdigit():
            listaPosicao.append(int(char))
        elif char in {',', '.', ';', ':', '(', ')', '{', '}', '[', ']', '@', '#', '$', '%', '&', '*', '?', '!', '_',
                      '=', '+', '-', '"', ' '}:
            listaPosicao.append(0)
        elif char == 'Ç':
            listaPosicao.append(3)
        else:
            for i in range(26):
                letra_atual = chr(ord('A') + i)
                if char == letra_atual:
                    listaPosicao.append(i + 1)

    return listaPosicao


contadorVogais = 0
contadorConsoantes = 0


def verificarVogaisEConsoantes(lista):
    global contadorVogais
    global contadorConsoantes
    for char in lista:
        char = char.upper()
        if char in {',', '.', ';', ':', '(', ')', '{', '}', '[', ']', ' ', 'Ç', '@', '#', '$', '%', '&', '*', '?', '!',
                    '_', '=', '+', '-', '"', ' '}:
            break
        elif char in {'A', 'E', 'I', 'O', 'U'}:
            contadorVogais = contadorVogais + 1
        else:
            contadorConsoantes = contadorConsoantes + 1

def limparVogaisEConsoantes():
    global contadorVogais
    global contadorConsoantes

    contadorVogais = 0
    contadorConsoantes = 0

def verificarMaiorLetra(lista):
    letrasApenas = [letra for letra in lista if letra.isalpha() and letra.upper() >= 'A' and letra.upper() <= 'Z']

    if not letrasApenas:
        return 0

    maiorLetra = max(letrasApenas, key=lambda letra: letra.upper())
    maiorLetra = maiorLetra.upper()
    if maiorLetra in {'Á', 'À', 'Ã', 'Â'}:
        maiorLetra = 'A'
    elif maiorLetra in {'É', 'Ê'}:
        maiorLetra = 'E'
    elif maiorLetra in {'Í', 'Ì', 'Î'}:
        maiorLetra = 'I'
    elif maiorLetra in {'Ó', 'Ò', 'Õ', 'Ô'}:
        maiorLetra = 'O'
    elif maiorLetra in {'Ú', 'Û', 'Ü'}:
        maiorLetra = 'U'

    posicaoMaiorLetra = ord(maiorLetra) - ord('A') + 1
    return posicaoMaiorLetra
