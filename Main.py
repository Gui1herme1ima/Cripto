import Alfabeto
import Matriz
import Cripto
import TratamentoDeListas
import Descripto

def menu():
    return input("O que deseja fazer?\n"
                 "1 - Criptografar\n"
                 "2 - Descriptografar\n"
                 "3 - Sair\n\n"
                 "Digite a opção desejada: ")


def continuarCripto():
    return input("\nDeseja criptografar novamente?\n(S/N)\n")

def continuarDescripto():
    return input("\nDeseja descriptografar novamente?\n(S/N)\n")

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Verifica se o input não é vazio ou só espaços
            return user_input
        else:
            print("Entrada inválida. Por favor, digite algo.\n")

def criptografar():
    entrada = get_non_empty_input("Digite o que deseja criptografar: ")
    entradaConvEmChar = list(entrada)
    if len(entradaConvEmChar) < 2:
        entradaConvEmChar.append('0')
        entradaConvEmChar.append('0')
    elif len(entradaConvEmChar) < 3:
        entradaConvEmChar.append('0')

    lista = TratamentoDeListas.posicaoNoAlfabeto(entradaConvEmChar)
    TratamentoDeListas.limparVogaisEConsoantes()
    TratamentoDeListas.verificarVogaisEConsoantes(entradaConvEmChar)
    quantVogais = TratamentoDeListas.contadorVogais
    quantConsoantes = TratamentoDeListas.contadorConsoantes
    maiorLetra = TratamentoDeListas.verificarMaiorLetra(entradaConvEmChar)

    Matriz.recebeLista(lista, quantVogais, quantConsoantes, maiorLetra)
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
    palavraCriptografada = get_non_empty_input("Informe o que deseja descriptografar: ")
    Descripto.palavraCriptografada(palavraCriptografada)

    chave = get_non_empty_input("Informe o a chave de criptografia: ")
    Descripto.Chave(chave)

    continuar = continuarDescripto().upper()

    while continuar not in ["S", "N"]:
        print("Opção inválida! Por favor, digite S ou N.")
        continuar = continuarDescripto().upper()

    if continuar == "S":
        descriptografar()
    elif continuar == "N":
        print("Retornando ao menu...")
        main()
def main():
    inicio = menu()

    while inicio not in ["1", "2", "3"]:
        print("Opção inválida! Por favor, digite a Opção correta")
        inicio = menu()

    if inicio == "1":
        criptografar()
    elif inicio == "2":
        descriptografar()
    elif inicio == "3":
        print("\nAté Mais!")


# Inicia o programa chamando a função main
main()