import Alfabeto
import Matriz
def posicao_no_alfabeto(lista):
    # Convertemos a letra para maiúscula para lidar com maiúsculas e minúsculas de forma uniforme
    listaPosicao = []
    for char in lista:
        char = char.upper()

        if char.isdigit():
            listaPosicao.append(int(char))
        elif char in {',','.',';',':','(',')','{','}','[',']','@','#','$','%','&','*','?','!','_','=','+','-'}:
            listaPosicao.append(0)
        elif char == 'Ç':
            listaPosicao.append(3)
        else:
            for i in range(26):  # Existem 26 letras no alfabeto inglês
                letra_atual = chr(ord('A') + i)
                if char == letra_atual:
                    listaPosicao.append(i+1)

    return listaPosicao

contadorVogais = 0
contadorConsoantes = 0
def verificarVogaisEConsoantes(lista):
    global contadorVogais
    global contadorConsoantes
    for char in lista:
        char = char.upper()
        if char in {',', '.', ';', ':', '(', ')', '{', '}', '[', ']', ' ', 'Ç', '@','#','$','%','&','*','?','!','_','=','+','-'}:
            break
        elif char in {'A','E','I','O','U'}:
            contadorVogais = contadorVogais + 1
        else:
            contadorConsoantes = contadorConsoantes + 1



if __name__ == "__main__":
    entrada = input("Digite o que deseja criptografar: ")
    entradaConvEmChar = list(entrada)
    verificarVogaisEConsoantes(entradaConvEmChar)
    Matriz.recebeLista(posicao_no_alfabeto(entradaConvEmChar), contadorVogais, contadorConsoantes)
    Matriz.imprimirMatriz()