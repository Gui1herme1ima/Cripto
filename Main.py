import Alfabeto
def posicao_no_alfabeto(lista):
    # Convertemos a letra para maiúscula para lidar com maiúsculas e minúsculas de forma uniforme
    listaPosicao = []
    for char in lista:
        char = char.upper()

        if char.isdigit():
            listaPosicao.append(int(char))
        elif char in {',','.',';',':','(',')','{','}','[',']'}:
            print(char)
            listaPosicao.append(0)
        elif char == 'Ç':
            print(char)
            listaPosicao.append(3)
        else:
            for i in range(26):  # Existem 26 letras no alfabeto inglês
                letra_atual = chr(ord('A') + i)
                if char == letra_atual:
                    listaPosicao.append(i+1)

    print(listaPosicao)

def processar_lista_de_chars(lista):
    listaPosicao = []
    for char in lista:
        listaPosicao.append(posicao_no_alfabeto(char))
    print(listaPosicao)




entrada = input("Digite o que deseja criptografar: ")

entradaConvEmChar = list(entrada)

posicao_no_alfabeto(entradaConvEmChar)