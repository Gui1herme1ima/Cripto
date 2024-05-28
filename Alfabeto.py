import random

alfabeto0 = ['T', 'ò', 'Ò', 'Â', 'i', 't', 'v', '(', 'S', 'R', 'M', 'ç', 'Õ', 'o', '}', 'è', 'á', 'Ê', 'j', 'n', '.',
             'B', 'Ç', '8', 'Ú', 'w', 'e', 'X', 'Ó', 'É', 'Ô', 'N', '0', '#', 'E', '%', 'U', 'Î', '&', 'Q', ')', 'k',
             'J', 'c', 'ù', 'p', 'h', '+', 'l', 'd', '=', '"', 'ô', 'C', ';', '@', ':', 'H', 'Y', 'Ù', 'ì', 'ó', '2',
             'a', 'Ì', 'V', 'Ï', 'í', '-', 'D', '7', 'È', 'q', 'f', 'r', '*', 'P', 'L', 'à', '6', 'y', 'Z', 'x', '[',
             'F', 'z', 'û', 'ã', 'G', ',', '3', 'Ã', 'b', '?', 'Í', ']', 'A', 'ê', 'é', 'À', 'õ', '5', 'u', 'Á', 'O',
             '_', 'â', 'ú', '$', 'm', 'I', 's', '9', 'W', '!', '4', '1', 'K', 'g', '{']
chaves0 = ['nR4oPq2Su9', 'I3aSbVxKd5', 'w1mPjYqZ30', 'H8aXoBc2Nk', '7bMqF5pL3s', 'uW2cJlVAe4', '5fRnZpU18h',
           'gQ6yDl3Fm0', 'L7rCt9XwV6', 'a9EiPdU8r3']

alfabeto1 = ['!', '+', '[', ',', 'Ï', '8', ':', 'M', '=', 'Õ', 'i', 'Î', ']', 'ù', 'D', 'ú', '5', 'Y', 'ô', '"', 'õ',
             'a', 'c', 'Ê', '}', 'Í', 'ò', '_', 'b', 'O', '7', '$', 'ì', 'Ç', 'n', 'B', ';', 'w', 'Á', 'J', '{', '@',
             'F', 'ã', 'T', 'Z', '2', '*', '0', 'E', 'r', 'k', 'í', '#', 'à', '-', 'Ì', 'm', '6', 'ó', 'Ô', '4', 'p',
             'f', 'z', 'y', 'R', 'U', 'N', 'É', 'é', 'S', 'X', '9', '.', 'H', 'q', 'À', 'e', 'x', '?', '3', 'o', '%',
             'Ù', 'A', 'è', 'C', '(', 't', 'l', 'ç', '&', 'á', 'h', 'I', 'ê', 'K', 'v', 'û', 'P', 'u', 'Ã', 'Ò', 'g',
             '1', 'G', 'j', 's', 'È', 'd', ')', 'Ó', 'Q', 'â', 'L', 'V', 'Â', 'W', 'Ú']
chaves1 = ['mPw6dA1vBz', 'S3rYjKbV9T', '7aPqZlXcN8', 'I2fUoHsR0G', 'aE4nWxL5uJ', 'bCtQm7gF1i', '9oRk3pDlYh',
           'H6wVzN8jTs', '4yM5uIqJdX', 'nG8pAeKsFt']

alfabeto2 = ['Ã', 'y', 'é', '5', 'í', 'r', 'Ô', 'N', 'D', 'Í', 'R', 'Ú', 'z', 'E', 'u', 'ò', 'G', 'i', 'ù', 'f', 'Ò',
             'v', 'ó', '9', 'e', 'Ç', '}', 'O', 'U', ']', 'Â', 'ã', 'H', '(', 'c', '!', 'q', 'm', 'I', 'C', 'P', ')',
             'ú', 'Z', '0', 'l', 'd', '*', 'b', 'ç', 'á', 'S', 'Y', 'Ì', 'j', 'Õ', '1', 'â', '%', 'à', 'É', 'Ê', '[',
             'ì', 't', 'W', 'J', '7', 'o', 'È', 'B', '?', '$', 'K', 'n', 'Á', '&', 'ê', 'Ó', 'k', '"', 'M', 'A', '2',
             'Q', 'a', 'è', '.', '#', 'g', '8', 'õ', '+', 'T', '4', ':', 'Ù', '-', 'ô', 'À', 'V', '3', '6', 'Î', '@',
             's', 'w', 'X', 'F', ',', 'p', '_', 'h', ';', 'x', '{', 'L', 'û', 'Ï', '=']
chaves2 = ['oZ4xR2mEhD', 'I8uKwN9vPc', '5lQsGfU6kT', 'H3eCqP0yMv', 'rV7bFgJdA2', 'uXtWmS5zLq', 'nYp4wU9kHj',
           'aBc6lEiJ8o', 'T1sPvR3xKf', 'IhAeG7dVjM']

alfabeto3 = ['ú', '{', 'X', '+', '_', 'g', '?', 'A', 'L', 'Â', '-', '5', 'N', 'w', 'Ì', '8', 'õ', 'Ã', '0', 'p', 'é',
             'h', 'M', 'É', 'b', 'c', '=', 'j', 'Ô', 'Ï', 'Ù', ',', '#', 'Z', 'f', '$', 'o', ')', 'V', '[', '@', 'O',
             '1', 'B', 'ò', 'x', 'I', 'u', 'T', 'Ç', 'n', 'm', 'y', 'Ò', 'í', 'a', '9', 'ô', ':', '%', 'E', 'z', 'È',
             '"', 'd', 'H', 'k', 'À', 'R', 'l', '.', 'P', 'â', 'D', '3', '}', 'Á', 'K', 'ç', 'v', 'ù', 'e', 'Y', 'Ú',
             's', '6', 'Õ', 'Q', '2', 'á', 'i', 'ã', ']', '*', 'r', 'U', 'S', 'Ó', '!', '&', 'è', ';', 'G', 'à', '4',
             'q', 'Í', '(', 'J', 'Î', 'û', 'Ê', 'ê', 'F', '7', 'W', 'C', 't', 'ì', 'ó']
chaves3 = ['qJkH8yPmL1', 'I7fCvN5jZt', 'oXbE4sNwF6', 'rA2jM5gWuQ', '3nFyGtB6dH', '7wTlQo8iVc', 'U1eKsW4hYj',
           'iD3bS8pRzV', 'gMlNtU5qE2', '9kPcHvJxIa']

alfabeto4 = ['i', '!', 'Õ', 'x', 'Ì', 'û', 'Ù', 'K', '%', 'h', 'à', 'I', ';', '}', 'Ê', 'l', 'M', '5', '4', 'w', 'L',
             's', '@', '[', 'z', 'ì', '?', '9', 'Ô', 'O', '7', '.', ',', '+', 'j', 'p', '(', 'Í', 'Z', 't', 'Q', '3',
             'Ú', 'Ã', '0', 'v', '&', 'E', 'o', '=', 'c', '_', 'T', 'n', 'd', 'Ï', '#', 'e', 'P', '1', 'u', 'Â', 'Y',
             'Á', ':', 'U', 'S', 'á', 'X', 'm', 'C', ']', '*', 'r', 'ò', 'É', 'f', 'í', 'G', 'B', 'H', 'â', 'ù', ')',
             'R', '8', '2', 'N', 'Ó', 'ã', 'ô', 'W', 'D', 'Ò', '$', 'a', 'À', 'Ç', 'è', '6', 'V', 'q', 'F', 'õ', 'k',
             '{', 'é', 'ê', 'Î', 'ó', 'g', 'b', 'y', 'ç', 'J', '"', '-', 'ú', 'È', 'A']
chaves4 = ['qF3wK6lBvG', '8dUcWbJ1hV', 'rP5eXoZjIa', '7fHqN2mRdW', 'lEiJ1oF3cK', 'tQpV4gX9yM', 'dS6nA8vYzR',
           'TmV7fDjN5k', 'uG8rH1wQsZ', 'wL3xK4tIqP']

alfabeto5 = ['E', ',', 'Á', 'R', 'ô', '-', 'k', 't', '(', 'z', '"', 'ê', '[', 'a', 'c', '8', 'F', '7', 'b', 'n', 'Õ',
             '@', '+', 'é', 'ù', 'É', '3', 'x', 'o', '=', 'ò', 'Q', 'r', 'P', 'Ç', 'T', 'û', 'È', 'A', '2', 'è', 'Ù',
             ']', 'D', 'm', '{', 'g', 'Â', 'd', 'J', 'U', '}', 'Ú', 'v', '6', '5', '4', 'l', 'Y', '_', ':', 's', '%',
             'V', 'u', '.', '!', 'N', ')', 'w', 'f', 'ó', 'O', 'Ò', 'Ì', 'X', 'Î', 'y', '?', 'Ê', 'à', 'K', 'Ó', 'í',
             'Ô', 'S', 'À', 'ì', '#', 'Z', '0', 'â', 'e', 'G', 'L', '&', 'i', 'Ï', 'I', 'á', 'B', 'W', 'h', ';', 'ã',
             'q', '*', 'p', '1', 'ç', 'j', 'H', 'ú', '$', '9', 'M', 'õ', 'Í', 'Ã', 'C']
chaves5 = ['jN1rL4xVfH', 'KmU9gE2sVl', 'aDqG5kXpC8', 'oW3lJtS9rN', '7hFyBpRjKd', 'TbA5dVnF3i', 'gQ6vYmZ2sW',
           'H8wE1tR4sG', 'cVnO9fP7zA', '6kIjY5xQhM']

alfabeto6 = ['7', 'ì', 'õ', '%', 'I', '9', 'è', 'E', 'Ù', 'Â', 'F', ']', 'B', 'ò', 'C', 'n', 'o', 'w', '[', 'Ú', 'r',
             '-', 'û', 'X', '3', '5', 'Ç', 'ã', '!', 'x', 'Î', 'â', 'Õ', 'ú', '0', 'u', '*', 'Ó', 'K', 'i', 'ê', '+',
             'z', 'm', 'J', '#', 'Í', 'q', '&', 'à', 'Ò', '}', 'L', '4', 'j', 's', 'D', 'c', 'y', ',', ')', '?', 'ó',
             'Q', 'ù', '1', 'Ô', '(', 'P', 'W', '6', 'A', 'ç', 'f', 'Z', 'í', 'V', 'l', 'd', '@', 'Ì', 'ô', 'R', 'À',
             ';', 'g', ':', 'Y', 'Ï', 'O', '.', 'k', 'G', 'b', 'É', '=', 'p', '$', 'é', 'T', 'È', 'v', 'Á', 'a', 'M',
             'e', 'S', '2', 'H', 'U', 't', 'N', 'Ê', '_', '8', 'Ã', 'h', 'á', '"', '{']
chaves6 = ['wV3sJbN9dU', 'cR8xPqTmLk', 'jN4gWqK6hX', 'yA1jE8zSfB', '9fD7wVbZiG', 'lH6qVtWjCm', 'sG3fJ8vMhT',
           'oR5dUkM7bN', 'PmL2tX6hNv', 'K9aCzWpTgS']

alfabeto7 = ['J', 'û', 'ã', 'A', 'í', 'b', '#', '!', 'Ï', 'É', 'Â', '7', 'ô', 'x', '4', 'S', 'G', '9', 'O', 'Ç', 'P',
             '$', '=', 'Õ', 'H', 'ú', 'j', '(', 'Ô', 'õ', '8', 'á', '*', '3', 'ê', 'ò', 'q', 'l', 'f', 'z', 'w', 'Á',
             'n', 'Î', ',', 'e', 's', ']', ';', 'p', 'é', 'K', '1', 'ó', 'D', 'è', 'X', 'M', 'Y', 'v', 'B', 'o', 'E',
             'ç', '5', '?', 'm', '}', 'L', 'g', 'y', 'h', 'r', 'R', 'c', '"', 'Ã', 'k', '-', '%', '.', 'à', '0', 'Ò',
             '_', '[', 'I', 'Q', 'F', 'U', 'W', '@', 'T', '+', 'u', '{', 'â', 'ì', 'Í', 'Z', 'Ù', 'Ê', '&', 'C', 'i',
             '6', 'd', ')', 'ù', 'N', 't', 'Ì', 'V', 'Ú', 'È', '2', 'a', 'Ó', 'À', ':']
chaves7 = ['qW5vA8tYkN', 'L6mJpI2rQo', 'V9wXnU5rZa', 'cE8uQlM6yS', 'G2tB7vYnCf', '9eVbJmW7sT', 'oD3jH4lQsX',
           'hN1tM2wRvZ', 'R7sL6bW9fX', 'gA4fN8wJkT']

alfabeto8 = ['3', 'x', 'F', 'ò', 'ó', 'r', 'f', 'E', ':', '9', 'T', 'õ', 'û', 'Ù', ';', 'A', 't', ')', '$', 'b', '@',
             'q', '+', '"', 'h', 'L', 'R', 'ù', '*', 'ô', 'Î', 'j', '4', 'a', 'Z', 'v', 'P', 'À', 'Ó', 'i', 'U', 'B',
             '-', 'Ì', 'o', 'Ò', 'e', 'Ç', 'd', 'Ï', '_', 'J', 'ú', 'u', 'Ô', 'â', 'ã', 'p', 'K', 'è', 'V', 'ê', 'm',
             'w', 'C', 'é', 'Í', 'Ú', 'ì', ']', 'ç', 'X', 'È', '%', '?', 'H', 'W', 'c', 'z', 'Â', 'g', 'É', 'I', ',',
             '2', 'Y', '7', '0', '(', '&', 'n', '5', 'à', '[', '.', 'S', 'Õ', 's', '6', 'O', 'k', '=', '8', 'Á', 'D',
             'l', '1', 'N', 'í', 'Ê', 'Ã', 'y', '#', 'G', 'á', '!', 'M', '}', 'Q', '{']
chaves8 = ['eS1mB8yZlT', 'N4gHkW3sJb', '8jPmDlXnW7', 'aE5dL7vYnF', 'K4cR3bAqUz', '2hYrCfQ8vA', 'W7tM9sH5kR',
           'V1zIgDqA3u', 'oF6nL2dHvP', 'J9xRtKpG4c']

alfabeto9 = ['N', '5', 'v', 'Î', 'ù', 'Q', '"', 'Õ', 'R', 'k', 'H', '!', ';', '?', '#', 'W', 'Â', 'y', 'x', 'Ì', ':',
             '3', 'ú', '*', '9', 'à', 'L', 'ó', '.', 'm', 'Ò', 'X', 'e', 'Ê', '+', 'Ù', 'j', '@', 'M', 'D', '1', 'í',
             'Ã', 'Ï', '(', 'u', 'Z', 'F', 'â', 'b', '=', 'ê', 'B', '_', ']', 'E', 'o', 'Ô', 'C', 'c', 'é', 'è', 'û',
             '[', 'i', 'Á', 'ç', 's', 'Ú', 'ò', '7', 'Í', 'À', '-', 'T', 'a', '0', 'ã', '6', 'q', 'O', 'á', '&', 'È',
             ')', 'V', 'h', 't', 'Ó', 'P', 'Y', 'É', 'f', 'r', '2', 'K', '}', 'I', 'l', ',', 'ì', '%', 'G', 'Ç', 'ô',
             'n', 'd', '{', 'z', 'A', 'õ', 'J', 'w', '4', 'g', 'U', 'p', '8', '$', 'S']
chaves9 = ['oP3nBf5gJl', 'T9mCzAqW7s', 'rL2yXwG6hV', 'kU8jDc4vNt', '5iSxR7zFpQ', 'qE1bHdY6mT', 'J4vNfP2aRg',
            'W3sXtZ8lDj', '7oKlQ9fA4b', 'aM6nGqV8iC']

tamanhoAlfabeto = len(alfabeto0)

todosOsAlfabetos = [alfabeto0, alfabeto1, alfabeto2, alfabeto3, alfabeto4, alfabeto5, alfabeto6, alfabeto7, alfabeto8,
                    alfabeto9]
todasAsChaves = [chaves0, chaves1, chaves2, chaves3, chaves4, chaves5, chaves6, chaves7, chaves8, chaves9]

numeroAlfabetoEscolhido = 0
def definirAlfabeto():
    global numeroAlfabetoEscolhido
    numeroAlfabetoEscolhido = random.randint(0, 9)
    alfabetoEscolhido = todosOsAlfabetos[numeroAlfabetoEscolhido]
    print(alfabetoEscolhido)
    print(f'o alfabeto escolhido foi o alfabeto{numeroAlfabetoEscolhido}')

    grupoDeChavesEscolhido = todasAsChaves[numeroAlfabetoEscolhido]
    numeroChaveEscolhida = random.randint(0,9)
    chaveEscolhida = grupoDeChavesEscolhido[numeroChaveEscolhida]

    return alfabetoEscolhido

def definirChave():
    global numeroAlfabetoEscolhido
    grupoDeChavesEscolhido = todasAsChaves[numeroAlfabetoEscolhido]
    numeroChaveEscolhida = random.randint(0, 9)
    chaveEscolhida = grupoDeChavesEscolhido[numeroChaveEscolhida]
    print(chaveEscolhida)

    return chaveEscolhida