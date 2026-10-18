"""
Algoritmos de Busca: Linear e Binária
Complexidade:
- Busca Linear: O(n)
- Busca Binária: O(log n) - requer lista ordenada
"""


def busca_linear(lista, alvo):
    """
    Realiza busca linear em uma lista.
    
    Args:
        lista: Lista de números para buscar
        alvo: Número a ser encontrado
        
    Returns:
        int: Índice do alvo se encontrado, -1 caso contrário
    """
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1


def busca_binaria(lista_ordenada, alvo):
    """
    Realiza busca binária em uma lista ordenada.
    
    Args:
        lista_ordenada: Lista de números ORDENADA para buscar
        alvo: Número a ser encontrado
        
    Returns:
        int: Índice do alvo se encontrado, -1 caso contrário
    """
    esquerda = 0
    direita = len(lista_ordenada) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1
