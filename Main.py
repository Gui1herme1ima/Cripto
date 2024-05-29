import Alfabeto
import Matriz
import Cripto
import TratamentoDeListas


def menu():
    return input("O que deseja fazer?\n"
                 "1 - Criptografar\n"
                 "2 - Descriptografar\n\n"
                 "Digite a opção desejada: ")


def continuarCripto():
    return input("\nDeseja criptografar novamente?\n(S/N)\n")


def criptografar():
    entrada = input("Digite o que deseja criptografar: ")
    entradaConvEmChar = list(entrada)
    if len(entradaConvEmChar) < 2:
        entradaConvEmChar.append('0')
        entradaConvEmChar.append('0')
    elif len(entradaConvEmChar) < 3:
        entradaConvEmChar.append('0')
    # RecebeLista(lista, quantVog, quantCons, MaiorLetra)

    lista = TratamentoDeListas.posicaoNoAlfabeto(entradaConvEmChar)
    quantVogais = TratamentoDeListas.contadorVogais
    quantConsoantes = TratamentoDeListas.contadorConsoantes
    maiorLetra = TratamentoDeListas.verificarMaiorLetra(entradaConvEmChar)

    TratamentoDeListas.verificarVogaisEConsoantes(entradaConvEmChar)
    Matriz.recebeLista(lista, quantVogais, quantConsoantes, maiorLetra)
    # Matriz.imprimirMatriz()
    Cripto.recebeEntrada(entradaConvEmChar)

    continuar = continuarCripto().upper()

    while continuar not in ["S", "N"]:
        print("Opção inválida! Por favor, digite S ou N.")
        continuar = continuarCripto().upper()

    if continuar == "S":
        criptografar()
    elif continuar == "N":
        print("Retornando ao menu...")
        main()


def descriptografar():
    print("Calmae q não fiz essa partekkkkkkkk")


def main():
    inicio = menu()

    while inicio not in ["1", "2"]:
        print("Opção inválida! Por favor, digite 1 ou 2.")
        inicio = menu()

    if inicio == "1":
        criptografar()
    elif inicio == "2":
        descriptografar()


# Inicia o programa chamando a função main
main()